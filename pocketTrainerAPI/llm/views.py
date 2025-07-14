from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiAPIView(APIView):
    def post(self, request):
        input_text = request.data.get("text")
        if not input_text:
            return Response({"error": "No text provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(input_text)
            return Response({"response": response.text}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

