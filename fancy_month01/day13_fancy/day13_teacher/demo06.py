"""
   当导入包时,需要在包的__init__.py文件中配置
"""

# 方式1:import 包
# 需要在包的__init__.py文件中配置:
#        import package01.package02.module02
#        from package01.package02.module02 import func01
import package01.package02 as p2
p2.module02.func01()
p2.func01()

# 方式2:from 包 import 包
from package01 import package02
package02.module02.func01()
package02.func01()
