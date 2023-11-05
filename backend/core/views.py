from json import JSONDecodeError # 用於處理 JSON 解碼時的錯誤
from django.http import JsonResponse # 建立包含 JSON 數據的 HTTP 響應
from .serializers import ContactSerializer 
from rest_framework.parsers import JSONParser # 解析 HTTP 請求中的 JSON 數據
from rest_framework import views, status # views 用於定義視圖，而 status 包含了 HTTP 狀態碼的定義
from rest_framework.response import Response  # 創建 HTTP 響應


class ContactAPIView(views.APIView):
    serializers_class = ContactSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
        }
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serilizer = ContactSerilizer(data=data)
            if serilizer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serilizer.data)
            else:
                return Respnse(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except JSONecodeErroe:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status= 400)