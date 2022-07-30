using System;

namespace Tri
{
    public class TriParInsertion
    {
		public static void tri_insertion_elementsPositifs(ref int[] tab, int taille)
		{
			int[] newTab = new int[taille];
			int i;
			for (i = 0; i < taille; i++) newTab[i] = -1;
			for (i = 0; i < taille; i++)
				if (tab[i] >= 0)
					newTab[i] = tab[i];
				else newTab[i] = 0;
			tab = newTab;
			int j;
			for (i = 1; i < taille; i++)
			{
				int elem = tab[i];
				for (j = i; j > 0 && tab[j - 1] > elem; j--)
					tab[j] = tab[j - 1];
				tab[j] = elem;
			}
		}

	}
}
