import java.util.Random;

public class RandomSequenceJava {

    public static void main(String[] args) {
        int sequenceLength = 128;

        Random random = new Random();

        for (int i = 0; i < sequenceLength; i++) {
            int randomNumber = random.nextInt(2);
            System.out.print(randomNumber);
        }

        System.out.println(); // перенос строки
    }
}