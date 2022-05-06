from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerialaizer
from .helper import jservice_request, date_conversion


class QuestionView(APIView):

    def get(self, request):
        questions = Question.objects.all()
        return Response({'questions': QuestionSerialaizer(questions, many=True).data})

    def post(self, request):
        # {"questions_num": int}
        question = Question.objects.all()
        serializer_data = QuestionSerialaizer(question.last()).data
        data = request.data
        num = data['questions_num']

        for item in jservice_request(num):
            while True:
                if item['id'] not in serializer_data:
                    id = item['id']
                    question_text = item['question']
                    answer = item['answer']
                    date_of_creation = date_conversion(item['created_at'])
                    Question.objects.create(
                        question_id=id,
                        question=question_text,
                        answer=answer,
                        date_of_creation=date_of_creation
                    )
                    break
                else:
                    item = jservice_request(1)[0]

        return Response({'question': serializer_data})
