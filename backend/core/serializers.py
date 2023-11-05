from . import models
from rest_framework import serializers
# 導入語句引入了用於定義序列化器字段的類型
from rest_framework.fields import CharField, EmailField

'''
序列化器定義了如何將 Contact 模型的資料轉換為 JSON 數據，
並確保 name、email 和 message 字段是必填的。
'''

class ContactSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)
    message = CharField(source="description", required=True)
    email = EmailField(required=True)

    class Meta:
        model = models.Contact
        fields = (
            'name', 
            'email',
            'message',
        )