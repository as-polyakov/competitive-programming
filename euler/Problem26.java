import java.util.*;

public class Problem26 {
    public static void main(String[] args) {
        int max = -1, d = -1;
        for(int i = 2; i < 1000; i++) {
            int m = period(i);
            if(m > max) {
                max = m;
                d = i;
            }
        }
        System.out.println(d + " period is " + max);
    }

    private static int period(int d) {
        Map<Integer, Integer> seen = new HashMap<>();
        int m = 1;
        int nn = 1;
        //System.out.print("0.");
        while(nn < 1000) {
            if(seen.containsKey(m) || m == 0)
                return (m == 0? 0 : nn - seen.get(m));
            seen.put(m, nn);
            while(m < d) {
                m *= 10;
                nn++;
            }
            nn--;
            int mm = m / d;
            //System.out.print(mm);
            m =  m - mm * d;
            nn++;
        }
        return -1;
    }
}
