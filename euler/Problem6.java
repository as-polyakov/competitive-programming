import java.util.stream.*;

public class Problem6 {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        System.out.println(bruteForce(n));
        System.out.println(math(n));
    }
    private static long math(int n) {
        long res = 0;
        for(int i = 1; i <= n; i++) {
            for(int j = i + 1; j <= n; j++ ) {
                res += i * j;
            }
        }
        return 2 * res;
    }
    private static long bruteForce(int n) {
        long s1 = IntStream.range(1, n + 1).map(i -> i * i).sum();
        long s2 = IntStream.range(1, n + 1).sum();
        return s2 * s2 - s1;
    }
}
