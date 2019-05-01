#
#1.HTTP経由でアップロードされたzip形式のモデルとモデル関連ファイルを
#  Brainから読み込み可能なように所定の場所に解答する機能
#
#2.解凍場所を設定ファイルから読み込む機能
#
#3.解凍場所にすでにあるモデルとモデル関連ファイルを削除して、
#  新たなものをBrainから読み込み可能なように展開する機能
#

import os
import zipfile
import shutil

#zipを解凍して所定の位置に配置
def unZip(zipfile, upDir, downDir):
	# upDir : 解凍元のdirectory
	# downDir : 解凍先のdirectory
	
	checkflg = False
	try:
	    #解凍場所のファイルの削除
	    shutil.rmtree(downDir)
	
	    #zipを読込から解凍
        with zipfile.ZipFile(os.path.join(upDir, zipfile)) as existing_zip:
            existing_zip.extractall(downDir)
        
        # success
        checkflg = True
        return checkflg
    
    except:
        
        # unsuccess
        checkflg = False
		return checkflg


