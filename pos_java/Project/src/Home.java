import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Home extends JFrame implements ActionListener {
    private JButton productbtn,customerbtn,orderbtn;
    private Container c;
    public Home() {
        super("Example Multiple Windows : Main Program");
        c = getContentPane();
        c.setLayout(new FlowLayout());  
        productbtn = new JButton(" App Product ");
        productbtn.addActionListener(this);
        c.add(productbtn);
        
        customerbtn = new JButton(" App Customer ");
        customerbtn.addActionListener(this);
        c.add(customerbtn);
        
        orderbtn = new JButton(" App Order");
        orderbtn.addActionListener(this);
        c.add(orderbtn);

        setSize(500, 400);
        getContentPane().setBackground(Color.darkGray);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == productbtn) {
            new AppProduct();
        } else if (e.getSource() == customerbtn){
            new AppCustomer();
        } else if (e.getSource() == orderbtn){
            new AppOrder();
        }    
    }
    public static void main(String[] args) {
        new Home();
    }

}
