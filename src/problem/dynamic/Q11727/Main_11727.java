package problem.dynamic.Q11727;
import java.io.*;

public class Main_11727 {
    static int d[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        d = new int[n+1];
        bw.write(Integer.toString(tiling(n)));

        bw.flush();
        bw.close();
        br.close();
    }
    public static int tiling(int n){
        if(d[n]>0)
            return d[n];
        if(n<=1){
            d[n] = 1;
        }
        else {
            d[n] = (tiling(n - 1) + tiling(n - 2)*2) % 10007 ;
        }
        return d[n];
    }
}
