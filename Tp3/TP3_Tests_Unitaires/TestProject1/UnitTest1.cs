using Microsoft.VisualStudio.TestTools.UnitTesting;
using Tri;

namespace TestProject1
{
    [TestClass]
    public class UnitTest1
    {
       
        [TestMethod]
        public void TestChemin1()
        {
            // chemin1)	2-4,  5,  6,  7,  10,  11,  12,  19
            int[] tableau = new int[0] {};
            int nombre = 0;
            TriParInsertion.tri_insertion_elementsPositifs(ref tableau, nombre);
            int[] tableauAttendu = new int[0] {};
            CollectionAssert.AreEqual(tableauAttendu, tableau);
        }

        [TestMethod]
        public void TestChemin2()
        {
            // chemin 2)	2-4 ,  5 ,  5’ ,  5 ,  6 ,  7 ,  10 ,  11 ,  12 ,  19
            // chemin reel  2-4 ,  5 ,  5’ ,  5 ,  6 ,  7 ,  8 ,  7’ ,  7 ,10 ,  11 ,  12 ,  19
            int[] tableau = new int[1] { 0 };
            int nombre = 1;
            TriParInsertion.tri_insertion_elementsPositifs(ref tableau, nombre);
            int[] tableauAttendu = new int[1] {0};
            CollectionAssert.AreEqual(tableauAttendu, tableau);
        }

        [TestMethod]
        public void TestChemin3()
        {
            // chemin 3)	2-4 ,  5 ,  6 ,  7 ,  8 ,  7’ ,  7 ,  10 ,  11 ,  12 ,  19
            // chemin reel  2-4 ,  5 ,  5’ ,  5 ,  6 ,  7 ,  8 ,  7’ ,  7 ,10 ,  11 ,  12 ,  19

            int[] tableau = new int[1] { 1};
            int nombre = 1;
            TriParInsertion.tri_insertion_elementsPositifs(ref tableau, nombre);
            int[] tableauAttendu = new int[1] { 1};
            CollectionAssert.AreEqual(tableauAttendu, tableau);
        }

        [TestMethod]
        public void TestChemin4()
        {
            // chemin 	2-4 ,  5 ,  6 ,  7 ,  9 ,  7’ ,  7 ,  10 ,  11 ,  12 ,  19
            // chemin reel  2-4 ,  5 ,  5’ ,  5 ,  6 ,  7 ,  9 ,  7’ ,  7 ,10 ,  11 ,  12 ,  19

            int[] tableau = new int[1] { -1 };
            int nombre = 1;
            TriParInsertion.tri_insertion_elementsPositifs(ref tableau, nombre);
            int[] tableauAttendu = new int[1] { 0 };
            CollectionAssert.AreEqual(tableauAttendu, tableau);
        }

        [TestMethod]
        public void TestChemin5()
        {
            // chemin  2-4 ,  5 ,  6 ,  7 ,  10 ,  11 ,  12 ,  13 ,  14 ,  15 ,  17 ,  18 ,  12 ,  19
            // chemin reel  2-4 ,5 ,6 ,7 ,10 ,11 ,12 ,13 ,14 ,15 ,17 ,18 ,12 ,13 ,14 ,15 ,17 ,18 ,19

            int[] tableau = new int[3] { 1, 2, 3 };
            int nombre = 3;
            TriParInsertion.tri_insertion_elementsPositifs(ref tableau, nombre);
            int[] tableauAttendu = new int[3] { 1, 2, 3 };
            CollectionAssert.AreEqual(tableauAttendu, tableau);
        }

        [TestMethod]
        public void TestChemin6()
        {
            // chemin 	2-4 ,  5 ,  6 ,  7 ,  10 ,  11 ,  12 ,  13 ,  14 ,  15 ,  16 ,  15 ,  17 ,  18 ,  12 ,  19
            //chemin reel 2-4 ,5 ,6 ,7 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,15 ,17 ,18 ,12 ,13 ,14 ,15 ,16 ,15 ,17 ,18 ,12 ,19

            int[] tableau = new int[3] { 2, 3, 1 };
            int nombre = 3;
            TriParInsertion.tri_insertion_elementsPositifs(ref tableau, nombre);
            int[] tableauAttendu = new int[3] { 1, 2, 3 };
            CollectionAssert.AreEqual(tableauAttendu, tableau);
        }
    }
}
