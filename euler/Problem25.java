import java.math.*;

public class Problem25 {
    public static void main(String[] args) {
        BigInteger f1 = new BigInteger("1"), f2 = new BigInteger("1"), f3 = f1.add(f2);
        for(int i = 3; ; i++) {
            f3 = f1.add(f2);
            f1 = f2;
            f2 = f3;
            if(f3.toString().length() == Integer.parseInt(args[0])) {
                System.out.println("F(" + i + ") = " + f3);
                break;
            }
        }
    }
}
