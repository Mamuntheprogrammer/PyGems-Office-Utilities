import sys
from cx_Freeze import setup, Executable
import os

# <added>
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# </added>

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('PyGems Office Utilities.py', shortcutName="PyGems Office Utilities",
            icon="icon.ico",base=base)
]


# Now create the table dictionary
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "PyGems Office Utilities",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]PyGems Office Utilities.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}

# <added>
options = {
    
          "bdist_msi": bdist_msi_options,

    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
	    'ficon.png','icon.ico',

         ],
         
        
    },
}
# </added>


setup(name = 'PyGems Office Utilities',
      version = "1.0",
      description = 'PyGems Office Utilities',
      # <added>
      author = 'MD : ABDULLAH AL MAMUN',
      author_email = 'pygemsbd@gmail.com',
      options = options,
      # </added>
      executables = executables
      )
