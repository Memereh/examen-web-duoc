--3 filas

/*
    Script para sacar el insert de la tabla TIPO_PRODUCTO copiar y pegar en la hoja de ejecucion ORACLE.

    DECLARE
        CURSOR CUR_TPRODUCTO IS SELECT * FROM TIPO_PRODUCTO;
    BEGIN
        FOR X IN CUR_TPRODUCTO LOOP
            dbms_output.put_line('INSERT INTO TIPO_PRODUCTO VALUES ('''||x.nombre||''');');
        END LOOP;
    END;

*/

INSERT INTO TIPO_PRODUCTO VALUES ('Alimento');
INSERT INTO TIPO_PRODUCTO VALUES ('Accesorio');
INSERT INTO TIPO_PRODUCTO VALUES ('Juguete');