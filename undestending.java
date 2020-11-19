import java.util.Random;
public class undestending {
    public static void main(String[] args) {
        int N=0;
        int tw_one = 0;
        int i = 0;
        int orel = 0,reshka = 0;
        int Y = 0;
        int X = 0;
        while (N<100000)
        {
            while (tw_one < 21) {
                Random rnd = new Random();
                int a = rnd.ints(0,2).limit(300).sum();;
                orel = a;
                reshka = 300 - a;
                if ((orel/reshka) >= (55/45))
                    X++;
                orel = 0;
                reshka = 0;
                tw_one++;
                }
            System.out.println("число случаев с орлом для соотношения (55/45) " + X);
            if (X == 20)
                Y++;
            tw_one = 0;
            X = 0;

            N++;
            }
        System.out.println("Число случаев " + (Y*1.0/N));
    }
}


