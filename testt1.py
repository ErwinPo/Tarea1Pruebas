#coding=utf-8
import unittest
from tarea1 import newbebida


class TestSum(unittest.TestCase):
    #TEST CASES:
    #El nombre del artículo es alfabético (válido)

    def test1(self):
        self.assertEqual(newbebida("aguita,1"), True)


    def test2(self):
        self.assertEqual(newbebida("4gu1t4,1"), False)

    #El nombre del artículo tiene menos de 2 caracteres de longitud (inválido)

    def test3(self):
        self.assertEqual(newbebida("normal,1"), True)
    
    def test4(self):
        self.assertEqual(newbebida("a,1"), False)

    #El nombre del artículo tiene de 2 a 15 caracteres de longitud (válido)

    def test5(self):
        self.assertEqual(newbebida("Aguita,1"), True)

    def test6(self):
        self.assertEqual(newbebida("aguita de limon con poca azucar,1"), False)

    #El valor del tamaño está en el rango de 1 a 48 (válido)

    def test7(self):
        self.assertEqual(newbebida("aguita,1"), True)

    def test8(self):
        self.assertEqual(newbebida("aguita,0"), False)

    def test9(self):
        self.assertEqual(newbebida("aguita,48"), True)

    def test10(self):
        self.assertEqual(newbebida("aguita,49"), False)

    #El valor del tamaño es un número entero (válido)

    def test11(self):
        self.assertEqual(newbebida("aguita,10"), True)

    def test12(self):
        self.assertEqual(newbebida("aguita,-1"), False)

    def test13(self):
        self.assertEqual(newbebida("aguita,-10"), False)

    #Los valores del tamaño se ingresan en orden ascendente (válido)

    def test14(self):
        self.assertEqual(newbebida("aguita,1,2,3"), True)

    def test15(self):
        self.assertEqual(newbebida("aguita,3,2,1"), False)

    def test16(self):
        self.assertEqual(newbebida("aguita,1,3,2"), False)

    #Se ingresan de uno a cinco valores de tamaño (válido)

    def test17(self):
        self.assertEqual(newbebida("aguita,1,2,3,4,5"), True)
    
    def test18(self):
        self.assertEqual(newbebida("aguita"), False)

    def test19(self):
        self.assertEqual(newbebida("aguita,1,2,3,4,5,6"), False)

    #El nombre del artículo es el primero en la entrada (válido)

    def test20(self):
        self.assertEqual(newbebida("1,aguita"), False)

    def test21(self):
        self.assertEqual(newbebida("aguita,1"), True)

    #Una sola coma separa cada entrada en la lista (válido)

    def test22(self):
        self.assertEqual(newbebida("aguita,1,2"), True)

    def test23(self):
        self.assertEqual(newbebida("aguita,,1"), False)
        
    def test24(self):
        self.assertEqual(newbebida("aguita,1,2,,"), False)

    #La entrada contiene o no espacios en blanco (a especificar en las pruebas)
    # (Ignora los espacios)

    def test25(self):
        self.assertEqual(newbebida("a g u i t a , 1 "), True)
    
    def test26(self):
        self.assertEqual(newbebida("aguita, 1, 2, 3, 4, 5"), True)

if __name__ == '__main__':
    unittest.main()