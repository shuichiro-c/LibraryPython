""" 
    FileUtility Module
"""
import os
import shutil   # fileCopy
from tkinter import messagebox
import tempfile
from typing import Union

#----------------------------------------------------------------

#----------------------------------------------------------------
class FileUtility:
    #------------------------------------------------
    # ファイル回り
    @staticmethod
    def CopyFileOverwrite(sourceFile:str, destinationFile:str) -> bool:
        """上書きありファイルコピー（フォルダも作成）"""
        sourceFile = FileUtility.PathConvert(sourceFile)
        destinationFile = FileUtility.PathConvert(destinationFile)

        if sourceFile == destinationFile:
            return False

        if FileUtility.IsExistFile(sourceFile) is False:
            return False
        
        # 出力先フォルダの作成
        FileUtility.CreateFolderFromFile(destinationFile)

        # ファイルがあれば削除
        if FileUtility.IsExistFile(destinationFile) is True:
            os.chmod(destinationFile,0o666)
            os.remove(destinationFile)

        # コピー
        shutil.copy2(sourceFile, destinationFile)
        os.chmod(destinationFile,0o666)

        return True

    @staticmethod
    def MoveFile(sourceFile:str, destinationFile:str) -> bool:
        """ファイル移動（フォルダも作成）"""
        sourceFile = FileUtility.PathConvert(sourceFile)
        destinationFile = FileUtility.PathConvert(destinationFile)

        if sourceFile == destinationFile:
            return False

        if FileUtility.IsExistFile(sourceFile) is False:
            return False
        
        # 出力先フォルダの作成
        FileUtility.CreateFolderFromFile(destinationFile)

        # ファイルがあれば削除
        if FileUtility.IsExistFile(destinationFile) is True:
            os.chmod(destinationFile,0o666)
            os.remove(destinationFile)

        # コピー
        shutil.move(sourceFile, destinationFile)
        os.chmod(destinationFile,0o666)

        return True


    @staticmethod
    def IsExistFile(file:str) -> bool:
        """ファイルの有無判定"""
        file = FileUtility.PathConvert(file)
        return os.path.exists(file)

    @staticmethod
    def DeleteFile(file:str) -> None:
        """ファイルの削除"""
        file = FileUtility.PathConvert(file)
        if FileUtility.IsExistFile(file) is True:
            os.chmod(file,0o666)
            os.remove(file)

    @staticmethod
    def IsOverwrite(file:str) -> bool:
        """ファイルの上書き確認"""
        file = FileUtility.PathConvert(file)

        if FileUtility.IsExistFile(file) is False:
            return True

        if messagebox.askyesno("OverWrite", file + "\n上書きしますか? ") is True:
            os.chmod(file,0o666)
            os.remove(file)
            return True
        
        return False

    @staticmethod
    def GetFileName(file:str) -> str:
        """ファイル名のみの取得"""
        file = FileUtility.PathConvert(file)
        return os.path.basename(file)

    @staticmethod
    def GetFileNameWithoutExtension(file:str) -> str:
        """ファイル名を拡張子なしで取得"""
        file = FileUtility.PathConvert(file)
        file, ext = os.path.splitext(os.path.basename(file))
        return file

    @staticmethod
    def GetFileExtension(file:str) -> str:
        """ファイル名の拡張子の取得"""
        file = FileUtility.PathConvert(file)
        root, ext = os.path.splitext(file)  # tupleで返ってくる
        return ext

    @staticmethod
    def GetFileList(folder:str) -> list[str]:
        """指定されたフォルダ内のファイルリストを返す"""
        folder = FileUtility.PathConvert(folder)
        fileList:list[str] = [
            f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))
        ]
        return fileList
    
    @staticmethod
    def GetFileSize(file:str) -> int:
        """ファイルサイズの取得"""
        file = FileUtility.PathConvert(file)
        return os.path.getsize(file)

    @staticmethod
    def getFileListExtension(folder:str, extension:str) -> list[str]:
        """指定されたフォルダ内のファイルリストを返す(拡張子選別)"""
        files_ext:list[str] = []
        tempFiles = FileUtility.GetFileList(folder)
        for file in tempFiles:
            if FileUtility.GetFileExtension(file) == extension:
                files_ext += {file}

        return files_ext

    #------------------------------------------------
    # フォルダ周り
    @staticmethod
    def CreateFolder(folder:str) -> None:
        """フォルダ作成"""
        folder = FileUtility.PathConvert(folder)
        if FileUtility.IsExistFolder(folder) is False:
            os.makedirs(folder)

    @staticmethod
    def CreateFolderFromFile(file:str) -> None:
        """フォルダ作成"""
        # 出力先フォルダの作成
        file = FileUtility.PathConvert(file)
        folder:str = os.path.dirname(file)
        FileUtility.CreateFolder(folder)

    @staticmethod
    def ReCreateFolder(folder:str) -> None:
        """フォルダ作成"""
        # フォルダの再作成
        folder = FileUtility.PathConvert(folder)
        if FileUtility.IsExistFolder(folder):
            shutil.rmtree(folder)
        FileUtility.CreateFolder(folder)

    @staticmethod
    def ReCreateFolderFromFile(file:str) -> None:
        """フォルダ作成"""
        # ファイル名から出力先フォルダの再作成
        file = FileUtility.PathConvert(file)
        folder:str = os.path.dirname(file)
        FileUtility.ReCreateFolder(folder)

    @staticmethod
    def IsExistFolder(folder:str) -> bool:
        """フォルダの有無判定"""
        folder = FileUtility.PathConvert(folder)
        return os.path.exists(folder)

    @staticmethod
    def GetDirectoryName(filepath:str) -> str:
        """指定されてファイルパスのディレクトリを返す"""
        return os.path.dirname(filepath)+"/"

    @staticmethod
    def GetDirectoryList(folder:str) -> list[str]:
        """指定されたフォルダ内のディレクトリリストを返す"""
        folder = FileUtility.PathConvert(folder)
        directryList:list[str] = [
            f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))
        ]
        return directryList


    #------------------------------------------------
    # その他
    @staticmethod
    def PathConvert(pathString:str) -> str:
        """パスセパレータの変換"""
        return pathString.replace("/","\\")

    @staticmethod
    def PathConvertReverse(pathString:str) -> str:
        """パスセパレータの変換"""
        return pathString.replace("\\","/")

    @staticmethod
    def PathNomalize(pathString:str) -> str:
        """不正になるファイル名を変換"""
        tmp = pathString.replace("[","")
        tmp = tmp.replace("]","")
        tmp = tmp.replace(" ","")
        return tmp

    @staticmethod
    def CopyTempFile(filepath:str) -> Union[str, bool]:
        """テンポラリに一時保存"""
        with tempfile.NamedTemporaryFile(delete=False) as n:
            #Log.message(n.name)
            # コピー
            if FileUtility.IsExistFile(filepath):
                shutil.copy2(filepath, n.name)
                os.chmod(n.name,0o666)
                return n.name
        
        return False
    
    @staticmethod
    def CreateTempFolder() -> str:
        return tempfile.mkdtemp()


#-------------------------------------------------------
# End of file.
#-------------------------------------------------------
