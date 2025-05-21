"""
    libHTTP.py
"""

import urllib.parse
import urllib.request
import urllib.error
from typing import Union

#----------------------------------------------------------------
class HTTPUtility():
    #----------------------------------------------------------------
    # URLの判定
    @staticmethod
    def isValid(url:str) -> bool:
        try:
            urllib.request.urlopen(url)
            return True
        except:
            return False

    #----------------------------------------------------------------
    # 第一クエリのみを残して返す
    @staticmethod
    def parseURL(url:str) -> Union[str,bool]:
        #https://www.youtube.com/watch?v=aabbccdd&t=110s
        newURL = url.split('&')[0]
        if HTTPUtility.isValid(newURL) is False:
            return False

        return newURL

    #----------------------------------------------------------------
    # 指定クエリの取得
    @staticmethod
    def getQuery(url:str, key:str) -> str:
        queries = HTTPUtility.getQueries(url)
        for parameter in queries:
            if parameter[0] == key:
                return parameter[1]

        return ""

    #----------------------------------------------------------------
    # クエリリストの取得
    @staticmethod
    def getQueries(url:str) -> list:
        queries = []
        result = urllib.parse.urlparse(url)
        for parameter in result.query.split('&'):
            key = parameter.split("=")[0]
            value = parameter.split("=")[1]
            queries += [(key,value)]

        return queries

    #----------------------------------------------------------------
    # クエリリストの取得
    @staticmethod
    def getLastURL(url:str) -> str:
        result = urllib.parse.urlparse(url)
        targetPath = result.path
        aString = targetPath.split('/')
        return aString[len(aString) - 1]

#----------------------------------------------------------------