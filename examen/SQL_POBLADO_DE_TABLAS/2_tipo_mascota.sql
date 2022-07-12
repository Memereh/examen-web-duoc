-- 6 filas

/*
    Script para sacar el insert de la tabla TIPO_MASCOTA copiar y pegar en la hoja de ejecucion ORACLE.

    DECLARE
        CURSOR CUR_TMASCOTA IS SELECT * FROM TIPO_MASCOTA;
    BEGIN
        FOR X IN CUR_TMASCOTA LOOP
            dbms_output.put_line('INSERT INTO TIPO_MASCOTA VALUES ('''||x.nombre||''','''||x.imagen||''');');
        END LOOP;
    END;

*/



INSERT INTO TIPO_MASCOTA VALUES ('Gatos','mascotas/gato.jpg');
INSERT INTO TIPO_MASCOTA VALUES ('Perros','mascotas/perro.jpg');
INSERT INTO TIPO_MASCOTA VALUES ('Aves','mascotas/ave.jpg');
INSERT INTO TIPO_MASCOTA VALUES ('Reptil','mascotas/tortuga.jpg');
INSERT INTO TIPO_MASCOTA VALUES ('Acuaticos','mascotas/pez.png');
INSERT INTO TIPO_MASCOTA VALUES ('Exoticos','mascotas/hamster.png');

