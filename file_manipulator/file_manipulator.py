import sys
import os

def validate_filenames(filename1, filename2, check_exisrence=True, check_file=True):
    
    if not isinstance(filename1,str) or not isinstance(filename2,str):
        raise TypeError("ファイル名は文字列でなければいけません。")
    
    def _validate_filename(filename,filename_name):
        error_message = ""
        if check_exisrence and not os.path.exists(filename):
            error_message = f"{filename_name}:ファイルが存在しません。"
            return error_message
        if check_file and not os.path.isfile(filename):
            error_message = f"{filename_name}:ファイルではありません。"
            return error_message
        return error_message
    
    error_message1 = _validate_filename(filename1,"Filename1")
    return not (error_message1), error_message1

def validate_filename_and_nunber(filename1, number, check_exisrence=True, check_file=True):
    
    if not isinstance(filename1,str) or not isinstance(number,int):
        raise TypeError("ファイル名は文字列かつ、複製回数は数字でなければいけません。")
    
    def _validate_filename(filename,filename_name):
        error_message = ""
        if check_exisrence and not os.path.exists(filename):
            error_message = f"{filename_name}:ファイルが存在しません。"
            return error_message
        if check_file and not os.path.isfile(filename):
            error_message = f"{filename_name}:ファイルではありません。"
            return error_message
        return error_message
    
    error_message1 = _validate_filename(filename1,"Filename1")
    if error_message1:
        return False, error_message1

    return True,""

def validate_filenames_and_text(filename1, str1, str2, check_exisrence=True, check_file=True):
    
    if not isinstance(filename1,str) or not isinstance(str1,str) or not isinstance(str2,str):
        raise TypeError("ファイル名、置き換え対象は文字列でなければいけません。")
    
    def _validate_filename(filename,filename_name):
        error_message = ""
        if check_exisrence and not os.path.exists(filename):
            error_message = f"{filename_name}:ファイルが存在しません。"
            return error_message
        if check_file and not os.path.isfile(filename):
            error_message = f"{filename_name}:ファイルではありません。"
            return error_message
        return error_message
    
    error_message1 = _validate_filename(filename1,"Filename1")
    return not (error_message1), error_message1

def main():
    if sys.argv[1] == "reverse":
        filename1 = sys.argv[2]
        filename2 = sys.argv[3]
        result, error1 = validate_filenames(filename1,filename2)
        if not result:
            print(f"エラー：{error1}")
            return
        else:
            contents = ''
            with open(filename1) as f:
                contents = f.read()
            with open(filename2,'w') as f:
                f.write(contents[::-1])
            return 

    elif sys.argv[1] == "copy":
        filename1 = sys.argv[2]
        filename2 = sys.argv[3]
        result, error1 = validate_filenames(filename1,filename2)
        if not result:
            print(f"エラー：{error1}")
            return
        else:
            contents = ''
            with open(filename1) as f:
                contents = f.read()
            with open(filename2,'w') as f:
                f.write(contents)
            return

    elif sys.argv[1] == "duplicate-contents":
        filename1 = sys.argv[2]
        repeat_number_str = sys.argv[3]
        try:
            repeat_number = int(repeat_number_str)
        except ValueError:
            print("エラー：繰り返し回数は整数でなければいけません。")
            return
        result, error1 = validate_filename_and_nunber(filename1,repeat_number)
        if not result:
            print(f"エラー：{error1}")
            return
        else:
            try:
                contents = ''
                with open(filename1,'r') as f:
                    contents = f.read()
                with open(filename1,'w') as f:
                    for _ in range(repeat_number):
                        f.write(contents)
            except Exception as e:
                print(f"エラー：ファイルの読み込み中にエラーが発生しました。")
                return 
            return

    elif sys.argv[1] == "replace-string":
        filename1 = sys.argv[2]
        str1 = sys.argv[3]
        str2 = sys.argv[4]
        result, error1 = validate_filenames(filename1,str1,str2)
        if not result:
            print(f"エラー：{error1}")
            return
        else:
            contents = ''
            with open(filename1) as f:
                contents = f.read()
            with open(filename1,'w') as f:
                f.write(contents.replace(str1,str2))
            return
        
    else :
        print("エラー：無効な操作です。")
        return

if __name__ == "__main__":
    main()
