from django.db import models
from django.contrib.auth.models import(BaseUserManager,AbstractBaseUser,PermissionsMixin)

# Create your models here.

class UsuarioManager(BaseUserManager):
    #def create_user(self,email,password,first_name,last_name):
    def create_user(self,email,password):
        """
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password is not provided')
        """
        usuario=self.model(
            email=self.normalize_email(email),
            password=password,
            #first_name=first_name,
            #last_name=last_name,
        )

        usuario.is_active=True
        usuario.is_staff=False
        usuario.is_superuser=False

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,email,password):
        usuario=self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        usuario.is_active=True
        usuario.is_staff=True
        usuario.is_superuser=True

        usuario.set_password(password)
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(verbose_name="E-mail", max_length=194,unique=True)
    first_name=models.CharField(verbose_name="Nome",max_length=240)
    last_name=models.CharField(verbose_name="Sobrenome",max_length=240)
 
    is_active= models.BooleanField(verbose_name="Usuário ativo",default=True,)
    is_staff= models.BooleanField(verbose_name="Usuário equipe desenvolvimento",default=False,)
    is_superuser= models.BooleanField(verbose_name="Usuário superusuário",default=False,)
 
    objects = UsuarioManager()
 
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
 
    class Meta:
        verbose_name="Usuário"
        verbose_name_plural="Usuários"
        db_table='tb_usuario'
 
    def __str__(self):
        return self.email