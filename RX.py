"""
################################################################################
# CHARS:  {✓ , ? , > , ! , X}

#### EXT: RUN FILE
# TODO:
 #>  When Keyword for Calling specifiec function when condition comes True
 #>  Indent check for ":" with getting first-line-indent and start-line-indent
 #>  Split line by strings, check_syntax spliteds ,connect them again
 #>  Array
 #>  Improve switch & case: No break - Default
 #>  goto for For loops with naming For loops
 #>  do_when
 #>  Improve Exception Catching when runing file
 #>  reindent->rx for indent checking or opposite?
 #>  Do_While loop
 #>  Load Modules:
       #> If Error happens in Loading module, .py file will remains
 #?  Debug Function in (--debug for debug-only && -d for run+debug)
 #X  Catch Error in Running file
 #!  END OF LINES ERROR IN RED
 #✓  Until:if not --- Unless:while not --- foreach:for
###########
# NOTE:
 #>  Create RX App with Menu:
        #>  Create SuperLite Module
 #>  Generate:yield(:None)?
 #>  Save Cache ?
 #>  Option for run translated or import it (import will ignore "if __name__ ...")
 #>  CONST at the beginning?
 #>  Stop Imports?
 #>  New Errors Ext Color
 #>  Package installer like pip? (if 3rd-party modules)
 #>  def(:None)?
###########
# BUG:
 #>  CONSTs:
       #!  After NameError rest of code will be ignored
 #>  No Support for args
 #?  Errors in red Color
 #?  Ignore module loading output error
 #X  Get Remaining Args for PROGRAM
 #X  Terminal is slow for loading code from first each time
 #✓  why exe doesn't accept args
 #✓  0.35 seconds are spent for what
 #✓  if if statement is more than 1 line it will be indent error

########################################

# TODO (Release):
 #> Check instal:  PrependPath=1 (also for pip and scripts/*.exe)
 #> Make .exe with cxfreeze && copy .exe fileS in py/scripts dir
 #> Auto install famous 3rd-parties (requests-urllib3)
 #> ".rx" to ".exe" 

####
   #Loading Modules Are 10-1000x faster (But Tanslate Takes 0.4!)
################################################################################
"""

#] CHANGES
r"""
 C:\Users\IRANIAN\.vscode\extensions\ms-python.python-2020.8.105369\package.json   (1637)
 C:\Users\IRANIAN\.vscode\extensions\ms-python.python-2020.8.105369\snippets\python.json   (END)
 D:\Programs\Microsoft VS Code\resources\app\extensions\rx\language-configuration.json 13
 
 D:\Programs\Microsoft VS Code\resources\app\extensions\python\syntaxes\MagicPython.tmLanguage.json
 (1746 at the end) 276
 33    "include": "#class-declarations"
 280   "name": "storage.type.classx.python",
 1025  "class-declarations": {
 1751  "builtin-types": {
 1784   | include        (and much more)
 366   "rx-class-names": {
 362   "include": "#rx-class-names"
 1373  "function-declaration": {
"""
#] VS Ext
r"""
 git add . && git commit
 vsce publish VERSION
 brs326qo5vgc774pezvenvixu4sj3c2lbwgqv66uwzsopcocl6ea
 
 Colors:
  invalid.deprecated.backtick.python   red
  support.type.exception.python        green
  support.variable.magic.python        blue light
  variable.other.constant.ruby         dodger_blue!
  storage.type.class.python            blue dark
  support.function.builtin.python      yellow
  keyword.control.flow.python          purple
"""
#] WHEN APP READY
r"""
 %USERPROFILE%
 #setx /M path "%path%;E:\ramin\Coding\GitHub\RX-Language"
 #C:\Users\IRANIAN\AppData\Roaming\ActiveState\bin;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\ProgramData\chocolatey\bin;D:\Programs\Coding\Git\cmd;C:\Users\IRANIAN\AppData\Local\Programs\Python\Python37;C:\Users\IRANIAN\AppData\Local\Programs\Python\Python37\Scripts;D:\Programs\Microsoft VS Code\bin;C:\Users\IRANIAN\AppData\Local\GitHubDesktop\bin;C:\Users\IRANIAN\AppData\Roaming\npm
"""








import sys
import re
import time
import argparse
import datetime
import os


START_TIME = time.time()


import RX_SuperLite as rx



print = rx.style.print
Error = rx.style.log_error
#print(f'ImpRX7 :: {time.time()-START_TIME}','green')
t = rx.Record()

RX_PATH = rx.files.abspath(__file__)[:-6]
__version__ = '1.0.0'

CLASSES = (['files','System','random','style','record','terminal','Tuple'],
           ['Files','Random','Record','Terminal','system','style','Tuple']
            #'internet', 'Internet'
           )

LOADED_PACKAGES = []




#< Make Things Ready For Running >#   0.035
def Setup_Env():
    rx.files.mkdir('__RX_LIB__')
    rx.write('__RX_LIB__/__init__.py')
    rx.files.hide('__RX_LIB__')


#< List of all errors >#
class ERRORS:
    #TRACEBACK = 'Traceback (most recent call last):'
    class BaseDefinedError(Exception):
        def __init__(self, attribute, line_text, line_nom, File):
            print('Traceback (most recent call last):')
            print(f'  File "{File}", line {line_nom}, in <module>')
            print( '    '+line_text)
            Error(f"BaseDefinedError: '{attribute}' can not be defined after setting module [OPTIONS]")
            sys.exit()

    class NameError(Exception):
        def __init__(self, 
                File, attribute=None, value=None, line_text='', 
                line_nom=0, correct_list=[], msg=None):
            print( 'Traceback (most recent call last):')
            print(f'  File "{File}", line {line_nom}, in <module>')
            print( '    '+line_text)
            if not msg:
                print(f"NameError: '{attribute}' can not be {value}. Valid Choices: {correct_list}")
            else:
                Error(f"NameError: {msg}")
            sys.exit()
    
    class ConstantError(Exception):
        def __init__(self,
          Line_Nom=0, Line_Def=0, Line_Text='', Attribute='', File='', msg=None):
            print( 'Traceback (most recent call last):')
            print(f'  File "{File}", line {Line_Nom}, in <module>')
            print( '    '+Line_Text)
            end = msg if msg else f"Redefinition of '{Attribute}' (Already Defined At Line {Line_Def})"
            Error("ConstantError: "+ end)
            sys.exit()

    class IndentionError(Exception):
        def __init__(self,
          Line_Nom=0, Line_Text='', File=''):
            print( 'Traceback (most recent call last):')
            print(f'  File "{File}", line {Line_Nom}, in <module>')
            print( '    '+Line_Text)
            Error("IndentationError: expected an indented block")
            sys.exit()

    class UndefinedError(Exception):
        def __init__(self, msg='', File=''):
            print( 'Traceback (most recent call last):')
            print(f'  File "{File}", in/out <module>')
            print( 'UndefinedError: Something Went Wrong. ')#, end='')
            if msg:
                print('  Possible Error: ','red')
                print('    '+msg, 'red')
            else:
                print('  Please Check Your code for Possible Issues','red')
                print('  If You are Sure It is a Bug Please Report This to the Maintainer','red')
            sys.exit()

    class ModuleNotFoundError(Exception):
        def __init__(self, File, Name=None, line_text='', line_nom=0):
            print( 'Traceback (most recent call last):')
            print(f'  File "{File}", line {line_nom}, in <module>')
            print( '    '+line_text)
            Error(f"ModuleNotFoundError: No module named '{Name}'")
            sys.exit()

    class AttributeError(Exception):
        def __init__(self,File, Line_Nom, Line_Text, Module_Version, Attribute):
            print('Traceback (most recent call last):')
            print(f'  File "{File}", line {Line_Nom}, in <module>')
            print('    '+Line_Text)
            Error(f"AttributeError: module '{Module_Version}' has no attribute '{Attribute}'")
            sys.exit()

    class LoadError(Exception):
        def __init__(self, Module, error=False):
            print('Traceback (most recent call last):')
            print(f'  Loading Module "{Module}" Resulted in an Error', 'red' if error else 'default')
            if error:
                print(error)
            else:
                print(f'    Module {Module} Returned Output When Loading')
                Error(f'LoadError: Make Sure There is No Print/Output in Module "{Module}"')
            sys.exit()


#< Get Arguments >#
def Get_Args():

    print('ARGS:  '+str(sys.argv), 'green')
    print(os.getcwd())
    if len(sys.argv) == 1:
        Console()
        #Menu()
        sys.exit()

    #if len(sys.argv) > 3:
    #    print('Argument Parser Will be added in next versions','dodger_blue_1')
    #    sys.exit()



    parser = argparse.ArgumentParser(
        'RX', allow_abbrev=True,
        description='"RX Language Executer"',

    )

    parser.add_argument(
        '-i', '--info',
        action='store_true',
        help='Show information about running file (Verbose option in other apps)'
    )

    parser.add_argument(
        'FILE',
        metavar='FILE', type=str, nargs='?',
        help='File to execute with RX language'
    )

    parser.add_argument(
        '-o','--options',
        action='store_true',
        help='Show Options to Customize File-Run and Exit'
    )

    parser.add_argument(
        '-d',
        action='store_true',
        help='Debug file/code/syntax Before running it and print Mistakes in Red color'
    )

    parser.add_argument(
        '--debug',
        action='store_true',
        help='Debug-Only mode. This will not run file. It just Debugs it'
    )

    parser.add_argument(
        '-MT',
        action='store_true',
        help='Module Test. Not Very Usefull For Beginers'
    )

    parser.add_argument(
        '-T2P',
        action='store_true',
        help='Translate To Python'
    )

    """
    parser.add_argument(
        'PROG_ARGS',
        action='store', 
        nargs=argparse.REMAINDER)
    """

    args = parser.parse_args()
    
    if args.options:
        print('BASE OPTIONS:'                                                                                                , style='bold')
        print("  OPTION NAME       DEFAULT VALUE       DESCRYPTION"                                                          , style='bold')
        print('  Module-Name       sc                  Shortcut for RX Tools and functions (also "Modulename")'                            )
        print('  Method            normal              Method of loading tools.'                                                           )
        print('                                          Valid Choices: [normal,[lite,fast]] (also "Package-Version)"'                     )
        print('OPTIONS:'                                                                                                     , style='bold')
        print("  OPTION NAME       DEFAULT VALUE       DESCRYPTION"                                                                        )
        print('  Func_Type_Checker True                Check if argument of a function is in wrong type'                                   )
       #print('                                          (REGEX:  (func|function)-?(type|arg|param)-?(scanner|checker) )'                  )
        print('  Exit              True                Exit after executing the code or not'                                               )
        print(                                                                                                                             )
       #print('"OPTIONS" SHOULD BE DEFINED AFTER "BASE OPTIONS"'                                                             , style='bold')

        sys.exit()


    if args.debug:
        args.d = True

    #print('ARGS:  '+str(args))
    #sys.exit()
    return args.FILE, args.info, args.d, args.debug, args.MT, args.T2P#, args.PROG_ARGS


#< Menu >#
def Menu():
    NOW = str(datetime.datetime.now())
    print(f'RX v{__version__} Running on {rx.system.device_name()}::{rx.system.accname()}')
    print('''
        {1}--Console
        {2}--System Info
        {3}--Compile

    ''')


#< Interactive RX Shell >#
def Console():
    NOW = str(datetime.datetime.now())
    print(f'RX v{__version__} Running on {rx.system.device_name()}::{rx.system.accname()}')
    rx.terminal.set_title('RX - Console')
    def wait_for_input(prompt):
        answer= ''
        while not answer:
            answer = input(prompt)
        return answer

    from importlib import reload
    
    rx.system.chdir(RX_PATH)
    PRE= ['import rx7.lite as sc','print = sc.style.print']
    rx.write('_Console_.py', '\n'.join(PRE)+'\n')
    import _Console_
    while True:
        try:
            new = wait_for_input('RX:Console> ')
            if new.lower() in ('exit','quit','end'):
                rx.files.remove('_Console_.py')
                sys.exit()
        except (KeyboardInterrupt,EOFError):
            rx.files.remove('_Console_.py')
            sys.exit()

        rx.write('_Console_.py', new+'\n', 'a')
        
        try:
            reload(_Console_)
        except Exception as e:
            ERROR = str(e)
            if '(_Console_.py,' in ERROR:
                ERROR = ERROR[:ERROR.index('(_Console_.py,')]
            print(str(type(e))[8:-2]+':  ' + ERROR, 'red')
            rx.write('_Console_.py', '\n'.join(rx.read('_Console_.py').splitlines()[:-1])+'\n', 'w')

        if re.search(r'^print\s*\(', rx.read('_Console_.py').splitlines()[-1].strip()):
            rx.write('_Console_.py', '\n'.join(rx.read('_Console_.py').splitlines()[:-1])+'\n')


#< Reading File >#
def Read_File(filepath):
    if filepath and rx.files.exists(filepath):
        with open(filepath) as f:
            SOURCE = f.read().split('\n')
        return SOURCE + ['\n']
        import os
        print(os.path.abspath(filepath), 'red')
    print(f"RX> can't open file '{filepath}': No such file", 'red') #or directory
    sys.exit()


#< Module Name and Version  <Method,Module_Name,Print,Indent,Const> >#
def Define_Structure(SOURCE, FILE, DEBUG):
    #] Checking Indentation
    """    
     #INDENT_OUTPUT = rx.terminal.getoutput(f'python {RX_PATH}\\reindent.py -d -n '+FILE)
     INDENT_OUTPUT = rx.terminal.getoutput(f'python reindent.py {FILE}')
     if len(INDENT_OUTPUT):
        print('REINDENT')
        INDENT_OUTPUT = INDENT_OUTPUT.split('\n')
        if INDENT_OUTPUT[-1].startswith('tokenize.TokenError'):
            raise ERRORS.UndefinedError('SyntaxError: a parantheses is still open',FILE)
        elif INDENT_OUTPUT[-1].startswith('IndentationError'):
            LINE = INDENT_OUTPUT[-4]
            LINE_NOM = LINE[LINE.index('line ')+5:]
            raise ERRORS.IndentionError(LINE_NOM, INDENT_OUTPUT[-3][4:],FILE)
        else:
            print('\n'.join(INDENT_OUTPUT))
            sys.exit()
            raise ERRORS.UndefinedError
        LINE = INDENT_OUTPUT[-4]
        LINE_NOM = LINE[LINE.index('line ')+5:]
        raise ERRORS.IndentionError(LINE_NOM, INDENT_OUTPUT[-3][4:],FILE)
    """
    #{???}autopep8 -i script.py
    import IndentCheck
    IndentCheck.check(FILE)

    #< OPTIONS >#
    MODULE_VERSION  = 'rx7'
    MODULE_SHORTCUT = 'sc'
    PRINT_TYPE = 'print'
    TYPE_SCANNER = True
    #BASED = False

    for line in SOURCE[:7]:

        #< Get Shortcut Name >#
        if re.search(r'^((M|m)odule(-|_)?(N|n)ame)\s*:\s*\w+',line):
            #if BASED:
            #    raise ERRORS.BaseDefinedError('Modulename', line, SOURCE[:5].index(line), FILE)
            stripped = line[line.index(':')+1:].strip()
            if re.search(r'\w+', stripped).group() == stripped:
                MODULE_SHORTCUT = str(stripped)
            else:
                raise ERRORS.NameError(msg='Invalid Value For  modulename/module_name', File=FILE)
            SOURCE.remove(line)

        #< Get Version (Method) of Tools >#
        elif re.search(r'^(Method|Package(-|_)Version)\s*:\s*\w*', line):
            #if BASED:
            #    raise ERRORS.BaseDefinedError('Method/Version', line, SOURCE[:5].index(line), FILE)
            StripLow = line.strip().lower()
            if StripLow.endswith('lite') or StripLow.endswith('fast'):
                MODULE_VERSION = 'rx7.lite'
            elif not StripLow.endswith('normal'):
                stripped = line[line.index(':')+1:].strip()
                raise ERRORS.NameError(FILE, 'Method', stripped, line, SOURCE[:5].index(line), ['lite','normal'])
            SOURCE.remove(line)

        #< Print Function Method >#
        elif re.search(r'^Print\s*:\s*\w*', line):
            #BASED = True
            if line.strip().lower().endswith('stylized'):
                PRINT_TYPE = 'stylized'
            elif not line.strip().lower().endswith('normal'):
                stripped = line[line.index(':')+1:].strip()
                raise ERRORS.NameError(FILE, 'print', stripped, line, SOURCE[:5].index(line), ['lite','normal'])
            SOURCE.remove(line)

        #< Function Type Scanner >#          TODO: # Make it Shorter!
        elif re.search(r'^((F|f)unc|(F|f)unction)(-|_)?((T|t)ype|(A|a)rg|(P|p)aram)(-|_)?((S|s)canner|(C|c)hecker)\s*:\s*\w*', line):
            #BASED = True     # No Need to do it
            if line.endswith('False'):
                TYPE_SCANNER = False
            elif not line.strip().endswith('True'):
                raise ERRORS.NameError(FILE, 'func_type_checker', stripped, line, SOURCE[:5].index(line), "[True,False]")
            SOURCE.remove(line)

        #< Exit at the end >#
        elif re.search(r'^(End(-|_))?(Exit|Quit)\s*:\s*\w*', line):
            if line.strip().lower().endswith('false'):
                SOURCE.append('__import__("getpass").getpass("Press [Enter] to Exit")')
            elif not line.strip().lower().endswith('true'):
                stripped = line[line.index(':')+1:].strip()
                raise ERRORS.NameError(FILE, 'Exit', stripped, line, SOURCE[:5].index(line), ['True','False'])
            SOURCE.remove(line)

    SOURCE[0] = f'import {MODULE_VERSION} as {MODULE_SHORTCUT}'
    SOURCE.insert(1,f"print = {MODULE_SHORTCUT+'.style.print' if PRINT_TYPE=='stylized' else 'print'}")
    SOURCE.insert(2,'')


    #print(CONSTS)
    return (SOURCE, 
            MODULE_VERSION, MODULE_SHORTCUT,
            TYPE_SCANNER)


#< Syntax >#
def Syntax(SOURCE, 
           MODULE_VERSION ,  MODULE_SHORTCUT,
           TYPE_SCANNER   ,
           FILE):
    import os
    os.path.relpath

    CONSTS = set()
    Keywords = ('if' , 'elif' , 'except' , 'def', 
                'for', 'while', 'foreach', 'until', 'unless',
                'try', 'else' , 'switch' , 'class', 'case',
                )
    Skip = 0
    
    for Line_Nom,Text in enumerate(SOURCE, 1):

        #print(str(Line_Nom)+' '+Text)
        
        for item in CONSTS:
            striped = Text.strip()
            if re.search(rf'( |;|^$){item[0]}\s*(\[.+\])?\s*=\s*[^=]+', Text):  # \s*.+  {?} 
                if not striped.startswith('def ')  and  not striped.startswith('#'):
                    raise ERRORS.ConstantError(Line_Nom, item[1], striped, item[0], FILE)


        #] When Adding An Extra Line Like Decorators
        if Skip:
            Skip = Skip-1
            continue
        if Text.strip().startswith('#'):
            continue

        # Ignore Docstrings
        elif '"""' in Text  and  not ("'''" in Text and Text.index('"""')>Text.index("'''")):
            if not '"""' in Text[Text.index('"""')+3:]:
                for line_in_str,text_in_str in enumerate(SOURCE[Line_Nom:],1):
                    if '"""' in text_in_str:
                        Skip = line_in_str
                        #print(Skip)
        elif '"""' in Text:
            if not "'''" in Text[Text.index("'''")+3:]:
                for line_in_str,text_in_str in enumerate(SOURCE[Line_Nom:],1):
                    if "'''" in text_in_str:
                        Skip = line_in_str
                        #print(Skip)


        #] Importing Tools
        elif Regex:=re.search(r'^(?P<Indent>\s*)(I|i)nclude \s*(\w+,?|\*)?', Text):
            Indent = Regex.group('Indent')
            if re.search(r'^(I|i)nclude\s*\*', Text.strip()):
                Packages = list(CLASSES[0])
            else:
                Packages = re.split(r'\s*,\s*', Text)
                Packages[0]= Packages[0][len(Indent)+8:].strip()
            SOURCE.remove(Text)
            for package in Packages:
                if package not in CLASSES[0]+CLASSES[1]:
                    raise ERRORS.AttributeError(FILE,Line_Nom,Text,MODULE_VERSION,package)
                SOURCE.insert(Line_Nom-1, f'{Indent}{package} = {MODULE_SHORTCUT}.{package}')
            continue

        #] Func Type checker
        elif Text.strip().startswith('def ') and TYPE_SCANNER:
            indent = Text.index('def ')
            SOURCE.insert(Line_Nom-1, f'{" "*indent}@{MODULE_SHORTCUT}.Check_Type')
            Skip = 1

        #] Switch and Case
        elif Regex:=re.search(r'^\s*(?P<indent>\s*)(S|s)witch\s+(?P<VARIABLE>\w+)\s*:', Text):
            indent = len(Regex.group('indent'))
            
            rules = 0
            for nom2,line2 in enumerate(SOURCE[Line_Nom:], 1):
                if not line2:
                    continue
                if not re.search(r'^(?P<indent2>\s*)\w+', line2) and  not rules:
                    #new = len(re.search(r'^(?P<indent2>\s*)', line2).group('indent2'))
                    LAST_LINE = nom2 + Line_Nom -1
                    break
            else:
                LAST_LINE = -1

            SOURCE.remove(Text)
            for Line,snc in enumerate(SOURCE[Line_Nom-1:LAST_LINE], Line_Nom):
                SEARCH_VALUE = re.search(r'^(C|c)ase\s+(?P<VALUE>.+):\s*', snc.strip())
                if SEARCH_VALUE:
                    if re.search(r'^elif \w+\s+==', SOURCE[Line-1].strip()):
                        raise TypeError
                    else:
                        pass#SOURCE[Line-1] =   ' '*(indent+4) + SOURCE[Line-1]
                    
                    SOURCE[Line-1] = f'{(indent)*" "}elif {Regex.group("VARIABLE")} == {SEARCH_VALUE.group("VALUE")}:' #+4
            SOURCE.insert(Line_Nom-1, f'{(indent)*" "}if False:pass')

        #] Load User-Defined Modules
        elif Regex:=re.search(r'^(?P<indent>\s*)(L|l)oad \s*(\w+,?)?', Text.strip()):
            Indent = Regex.group('indent')
            Packages = re.split(r'\s*,\s*', Text)
            Packages[0]= Packages[0][4:].strip()
            
            print(Packages)
            SOURCE.remove(Text)
            for package in Packages:
                if rx.files.exists(f'{package}.rx7'):
                    pack_out = rx.terminal.getoutput(f'python RX.py {package}.rx7 -MT -T2P').strip()
                    if len(pack_out):
                        if re.search(r'^\w+Error', pack_out.splitlines()[-1]):
                            raise ERRORS.LoadError(package,pack_out.splitlines()[-1])
                        else:
                            raise ERRORS.LoadError(package)
                    
                    rx.files.move(f'{package}.py', f'__RX_LIB__/{package}.py')
                    LOADED_PACKAGES.append(package)
                    #SOURCE.insert(Line_Nom-1,f"from __RX_LIB__ import {package};{MODULE_SHORTCUT}.files.remove('__RX_LIB__/{package}.py')")
                    SOURCE.insert(Line_Nom-1,f"{Indent}{package} = {MODULE_SHORTCUT}.import_module('{package}.rx7')") #;{MODULE_SHORTCUT}.files.remove('__RX_LIB__/{package}.py')
                else:
                    raise ERRORS.ModuleNotFoundError(FILE, package, Text, Line_Nom)

        #] Memory Location of Object
        elif re.search(r'''[,\(\[\{\+=: ]&\w+''', Text): #[^a-zA-Z0-9'"]
            Search=re.search(r' ?&(\w+)', Text)
            SOURCE[Line_Nom-1] = Text.replace(Search.group(),f'hex(id({Search.group(1)}))')

        #] until & unless & foreach & func
        elif Reg:=re.search(r'until \s*(?P<Expression>.+):', Text.strip()):
            SOURCE[Line_Nom-1] = f"if not ({Reg.group('Expression')}):"
        elif Reg:=re.search(r'unless \s*(?P<Expression>.+):', Text.strip()):
            SOURCE[Line_Nom-1] = f"if not ({Reg.group('Expression')}):"
        elif Reg:=re.search(r'foreach \s*(?P<Expression>.+):', Text.strip()):
            SOURCE[Line_Nom-1] = SOURCE[Line_Nom-1].replace('foreach', 'for', 1)
        elif Reg:=re.search(r'func \s*(?P<Expression>.+)', Text.strip()):
            SOURCE[Line_Nom-1] = SOURCE[Line_Nom-1].replace('func', 'def', 1)

        #] Const Var
        elif Text.strip().startswith('Const '):
            #if Text.startswith(' '): raise LateDefine("'Const' Must Be Defined In The Main Scope")
            if re.search(r'^Const\s+([A-Za-z]|_)+\s*=\s*', Text.strip()):
                INDENT = re.search(r'Const\s+([A-Za-z]|_)+\s*=\s*', Text).start()
                striped = Text.strip()
                SOURCE.remove(Text)
                SOURCE.insert(Line_Nom-1, INDENT*' ' + striped[striped.index(' ')+1:])
                CONST = striped[striped.index(' '):striped.index('=')].strip()
                if CONST != CONST.upper():
                    #] maybe it should be just a warning
                    raise ERRORS.ConstantError(Line_Nom=Line_Nom, 
                                               Line_Text=Text.strip(), 
                                               File=FILE, 
                                               msg='Constant Variable Name Must be UPPERCASE')
                for item in CONSTS:  #] Check if Const X is already defined
                    if CONST == item[0]:
                        raise ERRORS.ConstantError(Line_Nom, item[1], Text.strip(), item[0], FILE)
                CONSTS.add((CONST, Line_Nom))
        
        #] Const Array
        elif re.search(r'^\w+\s*=\s*<.+>', Text.strip()):
            search = re.search(r'(?P<Indent>\s*)(?P<VarName>\w+)\s*=\s*<(?P<Content>.*)>', Text)
            Content = search.group('Content')
            TYPE_ERROR = False
            try:
                Content = eval(Content)
                if type(Content) != tuple:
                    TYPE_ERROR = True
            except NameError:
                pass
            except Exception as e:
                raise e from None
            #else:
            VarName = search.group('VarName')
            if TYPE_ERROR:
                #raise TypeError(f"ArrayConst can not be '{type(Content)}' type (Use 'Const' keyword)")
                Type_Content = str(type(Content))[8:-2]
                if DEBUG:
                    print(f"'<>' is for Arrays, Try to use 'Const' keyword for type ",'red', end='')
                    print(f"'{Type_Content}'  ({FILE}:{Line_Nom}:{VarName})", 'red')#, style='bold')
            CONSTS.add((VarName, Line_Nom))
            #print(SOURCE[Line_Nom-1], 'red')
            SOURCE[Line_Nom-1] = f'{VarName} = {Content}'
        
        #] Indent
        elif Text.strip().endswith(':'):#.startswith(Keywords):
            BREAK = False
            LINE = int(Line_Nom)
            T = str(Text)
            while not BREAK:
                if SOURCE[LINE-1].strip().endswith(':'):
                    BREAK = True
                else:
                    LINE += 1

            INDENT = len(re.search(r'^(?P<indent>\s*).*', Text).group('indent'))
            INDENT_START = len(re.search(r'^(?P<indent>\s*).*', SOURCE[LINE]).group('indent'))
            if INDENT_START <= INDENT:
                #print('RX_Err','red')
                raise ERRORS.IndentionError(Line_Nom+1, SOURCE[Line_Nom], FILE)
        



    return SOURCE


#< Verbose >#
def Add_Verbose(SOURCE, FILE):
    NOW = str(datetime.datetime.now())
    print(f'''Start RX Language at "{NOW[:NOW.rindex('.')+5]}"''')
    print(f'Running  "{FILE}"')
    print('\n')

    SOURCE.insert(0, f'ProgramStartTime= {START_TIME}')
    EXECUTE_TIME_TEXT = 'round(__import__("time").time()-ProgramStartTime,3)'
    SOURCE.insert(-1, 'EXECUTE_TIME_TEXT='+EXECUTE_TIME_TEXT) #{EXECUTE_TIME_TEXT-.35}/
    SOURCE.insert(-1, r'''print(f'\n\nExecution Time:  {EXECUTE_TIME_TEXT}\n')''')
    #print(SOURCE[-3])

    return SOURCE


#< Clean Everything Which is Not Needed >#
def Clean_Up():
    rx.files.remove(f'__RX_LIB__', force=True)
    rx.files.remove('_RX_Py.py')
    #rx.files.remov('__pycache__', force=True)

#import atexit
#atexit.register(Clean_Up)







#< START OF THE CODE >#
if __name__ == "__main__":
    try:
        #print(f'START :: {time.time()-START_TIME}','green')
        '''
        if time.time()-START_TIME>0.025:
            print('Run Speed is Very Low. Restarting App', 'red')
            sys.exit()
            rx.terminal.run('python '+' '.join(sys.argv))
            sys.exit()
        '''
        #rx.terminal.set_title('RX')
        print(t.lap())
        ARGS = Get_Args()  # {0:FILE , 1:info , 2:d , 3:debug, 4:MT, 5:T2P}  0.008
        print(f'ARGS :: {t.lap()}')
        FILE   = ARGS[0]
        #rx.cls()
        Setup_Env()  #] 0.03
        SOURCE = Read_File(FILE)
        SOURCE = Define_Structure(SOURCE, FILE, ARGS[2])
        #print(f'DefStr :: {t.last_lap()}','green')
        SOURCE = Syntax(SOURCE[0], SOURCE[1], SOURCE[2], SOURCE[3], FILE)
        if ARGS[1]:
            SOURCE = Add_Verbose(SOURCE, FILE)
        if rx.files.exists('_RX_Py.py'): rx.files.remove('_RX_Py.py')
        rx.write('_RX_Py.py', '\n'.join(SOURCE))
        rx.write('translated', '\n'.join(SOURCE))
        rx.files.hide('_RX_Py.py')
        #print(f'Write :: {t.last_lap()}','green')
        try:
            if ARGS[5]:
                if FILE:
                    rx.write(f'{FILE.split(".")[0]}.py', '\n'.join(SOURCE))
                else:
                    print('Error in Parsing(T2P): With -T2P You Need To Specify FILE', 'red')
            
            if not ARGS[3]:
                if FILE:
                    import os
                    #os.system('python _RX_Py.py')
                    print(f'B_Run :: {time.time()-START_TIME}','green')
                    rx.terminal.set_title(f'RX - {os.path.basename(FILE)}')
                    import _RX_Py
                else:
                    print('Error in Parsing(TM): No FILE is Given', 'red')
                    sys.exit()


        except Exception as E:
            if ARGS[4]:
                raise E
            #raise E
            print('Traceback (most recent call last):','red')
            print('  More Information Soon...','red')
            print(str(type(E))[8:-2]+': '+str(E), 'red', style='bold')
            '''
            print('Traceback (most recent call last):')
            print(f'  File "{FILE}" in  "UNDEFINED"')
            print(e, 'red')
            sys.exit()
            '''
        finally:
            Clean_Up()
            #rx.files.remove(f'__RX_LIB__', force=True)
            #rx.files.remove('_RX_Py.py')
            #rx.files.remove('__pycache__', force=True)            

    except KeyboardInterrupt:
        print('\nExiting Because of KeyboardInterrupt Error (Ctrl+C)','red')
