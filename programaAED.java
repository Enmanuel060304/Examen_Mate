import javax.swing.JOptionPane;

public class Main
{
    public static void main(String[] args)
    {
        String toString = String.format("Valores iniciales del arreglo %n");
        int [] valores = new int[Integer.parseInt(JOptionPane.showInputDialog("Ingresa cantidad de valores a ordenar"))];
        for (int i = 0; i < valores.length; i++)
        {
            valores[i] = Integer.parseInt(JOptionPane.showInputDialog("Ingresa valor para la posicion "+ (i + 1)));
            toString += String.format(valores[i]+"%n");
        }

        JOptionPane.showMessageDialog(null,ordenar(valores, toString),"Ordenamiento de un Array",1);
    }

    static String ordenar(int arreglo[], String texto)
    {

        for (int i = 0; i < arreglo.length; i++)
        {
            for (int j = 0, n = arreglo.length - 1;j < n; j++)
            {
                int actual = arreglo[j],
                        siguiente = arreglo[j + 1];

                if (siguiente < actual)
                {
                    arreglo[j] = siguiente;
                    arreglo[j + 1] = actual;
                }
            }
        }
        texto += String.format("Valores Ordenados %n");

        for (int i = 0; i < arreglo.length; i++)
        {
            texto += String.format(arreglo[i]+"%n");
        }
        return texto;
    }

}
