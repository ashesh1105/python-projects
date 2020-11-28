# Import from a specific module
from mymodule import myfunc

#Import from a package
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

# Calling function from specific module - myfunc
myfunc()

# Calling functions from main package
some_main_script.report_main()

# Calling functions from subpackage
mysubscript.sub_report()
