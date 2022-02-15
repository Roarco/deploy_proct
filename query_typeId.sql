-- query para insertar los tipos de documentos

INSERT INTO `typeId`(`description`)
VALUES('Cedula de Ciudadania'),('Cedula de Extranjeria'),('Certificado de Cabildo'),(
    'Documento de identidad Extranjera'
),('Nit'),('Pasaporte'),('Tarjeta de identidad')

-- query para insertar un administrative
INSERT INTO `Administrative`(
    `administrative_code`,
    `name`,
    `lastname`,
    `id_typeid`,
    `IDNumber`
)
VALUES(
    '7541713001',
    'Julanito',
    'Perez',
    '1',
    '110265986'
)

--query para insertar los estadosde documentos
INSERT INTO `State`(`description`)
VALUES('En revision'),('Rechazado'),('Aceptado')


--querys para postgrest

INSERT INTO public."typeId"(description)
VALUES('Cedula de Ciudadania'),('Cedula de Extranjeria'),('Certificado de Cabildo'),(
    'Documento de identidad Extranjera'
),('Nit'),('Pasaporte'),('Tarjeta de identidad')

INSERT INTO public."Administrative"(
	administrative_code, name, lastname, id_typeid, "IDNumber")
	VALUES ('7541713001',
    'Julanito',
    'Perez',
    '1',
    '110265986');

INSERT INTO public."State"( description)
	VALUES ('En revision'),('Rechazado'),('Aceptado');