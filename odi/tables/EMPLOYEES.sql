DROP TABLE hr.xx_employees;

CREATE TABLE hr.xx_employees
(
    employee_id            NUMBER( 6, 0 )
  , first_name             VARCHAR2( 20 )
  , last_name              VARCHAR2( 25 ) CONSTRAINT "EMP_LAST_NAME_NN" NOT NULL ENABLE
  , email                  VARCHAR2( 25 ) CONSTRAINT "EMP_EMAIL_NN" NOT NULL ENABLE
  , hire_date              DATE CONSTRAINT "EMP_HIRE_DATE_NN" NOT NULL ENABLE
  , salary                 NUMBER( 8, 2 )
  , manager_id             NUMBER( 6, 0 )
  , department_id          NUMBER( 4, 0 )
);