import java.lang.Math;

public class BBS {
    private static int p, q, seed, M, X;

    public static void main(String[] args) {
        if (args.length == 3) {
            p = Integer.parseInt(args[0]);
            q = Integer.parseInt(args[1]);
            seed = Integer.parseInt(args[2]);
            M = Math.multiplyExact(p, q);

            BBS();
        } else {
            System.err.println("Bad args...");
        }
    }

    public static int getX(int k) {
        return (int)Math.pow(k, 2) % M;
    }

    public static boolean isPrime(int value) {
        int end = (int)(Math.sqrt(value) + 1);
        boolean result = false;
        for (int i = 2; i < end; i++) {
            if(value % i == 0){
                result = false;
                break;
            }
            else {
                result = true;
                break;
            }
        }
        return result;
    }

    public static boolean isCongruent(int value) {
        if(value % 4 == 3) 
            return true;
        return false;
    }

    public static void BBS() {
        X = (int)Math.pow(seed, 2) % M;
        System.out.format("x0: %d\n", X);
        for(int i = 1; i < 40; i++) {
            X = getX(X);
            System.out.format("x%d: %d\n", i, X);
        }
    }
}