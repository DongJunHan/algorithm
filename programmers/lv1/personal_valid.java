import java.util.*;
public class personal_valid{
public List<Integer> solution(){
    //            String today = "2020.01.01";
    //            String[] privacies = {"2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"};
    //            String[] terms = {"Z 3", "D 5"};
    
        List<Integer> answer = new ArrayList<>();
        String today = "2022.05.19";
        String[] terms = {"A 6", "B 12", "C 3"};
        String[] privacies = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C", "2022.02.19 C","2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C","2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C","2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};
        int[] t_today = Arrays.stream(today.split("\\.")).mapToInt(Integer::parseInt).toArray();
        int s_today = (t_today[0]*12*28)+(t_today[1]*28)+t_today[2];
        Map<String, Integer> a = new HashMap<>();
        for (String t: terms) {
            Object[] z = Arrays.stream(t.split(" ")).toArray();
            a.put((String)z[0], s_today - (Integer.parseInt((String)z[1])) * 28);
        }
        for (int i=0; i < privacies.length; i++) {
            Object[] privace = Arrays.stream(privacies[i].split(" ")).toArray();
            int[] t_date = Arrays.stream(((String)privace[0]).split("\\.")).mapToInt(Integer::parseInt).toArray();
            int date = (t_date[0]*12*28)+(t_date[1]*28)+t_date[2];
            if (date <= a.get((String)privace[1])) answer.add(i+1);
        }
        return answer;
    }
}