from fastapi import APIRouter


affiliate_router = APIRouter


@ affiliate_router.delete("/user/delete", tags=["CRUD Affiliate"], dependencies=[Depends(JWTBearer())])
async def user_delete(current_user: Affiliate = Depends(get_current_Affiliate)):
    email = current_user.email
    user_drop = CD.delete_affiliate(email)
    if not user_drop:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proceso no se puede completar"
        )
    return {"detail": "El usuario ha sido eliminado"}


@ affiliate_router.post("/user/create", tags=["CRUD Affiliate"])
async def create_user(
    fullname: str = Form(...),
    document_type: str = Form(...),
    document_number: int = Form(...),
    birthdate: date = Form(...),
    email: str = Form(...),
    city: str = Form(...),
    password: str = Form(...),
    membership_type: str = Form(...),
    gender: str = Form(...),
    Address: str = Form(...),
    Clinical_history: str = Form(...),
    phone_number: int = Form(...)
):
    try:
        # Crear un objeto Affiliate
        user = Affiliate(
            fullname=fullname,
            document_type=document_type,
            document_number=document_number,
            birthdate=birthdate,
            email=email,
            city=city,
            password=password,
            membership_type=membership_type,
            gender=gender,
            Address=Address,
            Clinical_history=Clinical_history,
            phone_number=phone_number
        )

        # Crear el afiliado en la base de datos
        new_user = CD.create_affilite(user)

        if not new_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error al crear el usuario")

        return {"detail": "El usuario se ha creado con éxito"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno: {str(e)}")


@affiliate_router.put("/user/update", tags=["CRUD Affiliate"], dependencies=[Depends(JWTBearer())])
async def affiliate_update(
    address: str = Form(...),
    phone_number: str = Form(...),
    city: str = Form(...),
    password: Optional[str] = Form(None),
    current_user: Affiliate = Depends(get_current_Affiliate)
):
    # Extraemos el email del usuario actual
    email = current_user.email

    # Actualizamos los datos del afiliado
    update_result = CD.update_affiliate(
        email=email,
        address=address,
        phone_number=phone_number,
        city=city,
        password=password
    )

    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no se pudo actualizar"
        )

    return {"detail": "Affiliate updated successfully"}
