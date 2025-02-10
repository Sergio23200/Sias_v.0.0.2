from pydantic import BaseModel, Field


class login_schema_sign_up(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Ips_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    document_type: str = Field(required=True)
    document_number: str = Field(required=True)
    password: str = Field(required=True)
