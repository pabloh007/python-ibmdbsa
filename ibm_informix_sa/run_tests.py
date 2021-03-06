from sqlalchemy.dialects import registry

registry.register("db2", "ibm_informix_sa.ibm_db", "DB2Dialect_ibm_db")
registry.register("db2.ibm_db", "ibm_informix_sa.ibm_db", "DB2Dialect_ibm_db")
registry.register("db2.pyodbc", "ibm_informix_sa.pyodbc", "DB2Dialect_pyodbc")
registry.register("db2.zxjdbc", "ibm_informix_sa.zxjdbc", "DB2Dialect_zxjdbc")
registry.register("db2.pyodbc400", "ibm_informix_sa.pyodbc", "AS400Dialect_pyodbc")
registry.register("db2.zxjdbc400", "ibm_informix_sa.zxjdbc", "AS400Dialect_zxjdbc")

from sqlalchemy.testing import runner

runner.main()

