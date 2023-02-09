# 5. Напиши функцию на Python, выполняющую сравнение ерсий. Условия
# - Return -1 if version A is older than version B
# - Return 0 if version A and version B are equivalent
# - Return 1 if version A is newer than version B
# - Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.

from scripts.fifth import compare_versions

print(compare_versions('1.10', '1.1'))
print(compare_versions('1.8', '1.11'))
print(compare_versions('1.1', '1.1'))
