# Lab 5: Static Analysis Issues Fixed

## Summary
- **Initial Pylint Score**: 4.80/10
- **Final Pylint Score**: 10.00/10
- **Improvement**: +5.20 points
- **Total Issues Fixed**: 10+

## Issues Documentation Table

| Issue Type | Tool | Line(s) | Severity | Description | Fix Approach |
|------------|------|---------|----------|-------------|--------------|
| Dangerous default value | Pylint | 8 | **HIGH** | `logs=[]` mutable default argument shared across all function calls | Changed default to `logs=None` and initialize empty list inside function |
| Insecure function | Bandit | 59 | **MEDIUM** | `eval()` can execute arbitrary malicious code | Completely removed the eval() statement |
| Bare except clause | Pylint/Flake8/Bandit | 19 | **MEDIUM** | `except:` catches all exceptions including system exits and keyboard interrupts | Changed to `except KeyError:` with informative warning message |
| File not closed properly | Pylint | 26, 32 | **MEDIUM** | Files opened without context manager may not close on errors | Used `with open()` statement for automatic file closing |
| Unused import | Pylint/Flake8 | 2 | LOW | `logging` module imported but never used | Removed the unused import statement |
| Missing blank lines | Flake8 | Multiple | LOW | PEP 8 requires 2 blank lines between top-level functions | Added 2 blank lines between all function definitions |
| Function naming convention | Pylint | Multiple | LOW | Used camelCase instead of snake_case (e.g., `addItem` vs `add_item`) | Renamed all functions to follow snake_case convention |
| Missing docstrings | Pylint | All functions | LOW | No documentation strings for module or functions | Added comprehensive docstrings to module and all 8 functions |
| Old string formatting | Pylint | 12 | LOW | Using % formatting instead of modern f-strings | Changed to f-string: `f"{datetime.now()}: Added {qty} of {item}"` |
| Missing encoding parameter | Pylint | 26, 32 | LOW | open() called without explicit encoding specification | Added `encoding="utf-8"` parameter to all file operations |
| Global statement usage | Pylint | 68 | LOW | Usage of global statement flagged as potential code smell | Added suppression comment as global is necessary here |
| Missing final newline | Pylint | 131 | LOW | File should end with a blank line per PEP 8 | Added blank line at end of file |

## Priority Fixes (Minimum 4 Required)
1. ✅ **Mutable default argument** (HIGH) - Lines 8
2. ✅ **Insecure eval() usage** (MEDIUM) - Line 59  
3. ✅ **Bare except clause** (MEDIUM) - Line 19
4. ✅ **Improper file handling** (MEDIUM) - Lines 26, 32

## Additional Fixes (For Extra Credit)
5. ✅ Removed unused imports
6. ✅ Fixed all PEP 8 style violations
7. ✅ Renamed all functions to snake_case
8. ✅ Added comprehensive documentation
9. ✅ Improved string formatting
10. ✅ Added encoding specifications
11. ✅ Suppressed necessary global statement warning
12. ✅ Added final newline

**Result: ALL issues resolved - Perfect 10/10 score achieved! 🎉**