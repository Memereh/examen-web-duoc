--7 filas

/*
    Script para sacar el insert de la tabla PRODUCTOS copiar y pegar en la hoja de ejecucion ORACLE.

    DECLARE
        CURSOR CUR_PRODUCTO IS SELECT * FROM productos;
    BEGIN
        FOR X IN CUR_PRODUCTO LOOP
            dbms_output.put_line('INSERT INTO PRODUCTOS VALUES ('''||x.nombre||''','||x.precio||','||x.stock||','''||x.descripcion||''','||x.tipo_producto_id||','||x.tipo_mascota_id||','''||x.imagen||''');');
        END LOOP;
    END;

*/


INSERT INTO PRODUCTOS VALUES ('Master Dog - Alimento Perro Adulto Pollo',25640,100,'Alimento Perro Adulto Pollo',1,2,'productos/master_dog.jpg');
INSERT INTO PRODUCTOS VALUES ('Afp - Modern Cat Flash Ball Variedad de colores',4390,10,'Modern Cat Flash Ball Variedad de colores',3,1,'productos/JUGETE_GATO.jpg');
INSERT INTO PRODUCTOS VALUES ('Whiskas - Alimento Húmedo Sobrecito Gatitos Carne Soufflé',470,11,'Alimento Húmedo Sobrecito Gatitos Carne Soufflé',1,1,'productos/Whiskas.jpg');
INSERT INTO PRODUCTOS VALUES ('Nina Ottosson - Perro Puzzle Twister Nivel 3',28490,20,'Perro Puzzle Twister Nivel 3',3,2,'productos/Nina_Ottosson-Perro_Puzzle_Twister_Nivel_3_1.png');
INSERT INTO PRODUCTOS VALUES ('Cat It - Senses 2.0 Self-Groomer',6100,10,'Senses 2.0 Self-Groomer',3,1,'productos/22517431528_1.png');
INSERT INTO PRODUCTOS VALUES ('Cat Love - Baño Con Borde Celeste/Gris',11300,20,'Baño Con Borde Celeste/Gris',2,1,'productos/arenero.png');
INSERT INTO PRODUCTOS VALUES ('Afp - Monster Bunch Gorro Purpura',10900,40,'Monster Bunch Gorro Purpura',2,2,'productos/AfpMonsterBunchGorroPurpura_2.png');