import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.time.LocalDate;
import java.util.ArrayList;
import javax.swing.*;

public class AppOrder extends JFrame implements ActionListener {
    private JComboBox<String> customerBox, productBox;
    private JTextField quantityField;
    private JButton purchaseBtn;
    private JTextArea outputArea;
    private ArrayList<String[]> customers = new ArrayList<>();
    private ArrayList<String[]> products = new ArrayList<>();
    private static final String FILENAME_PRODUCTS = "products.txt";
    private static final String FILENAME_CUSTOMERS = "customers.txt";
    private static final String ORDER_FILE = "Order.txt";

    public AppOrder() {
        super("Order System");
        setLayout(new FlowLayout());

        customerBox = new JComboBox<>();
        productBox = new JComboBox<>();
        customerBox.addItem("Select a Customer");
        productBox.addItem("Select a Product");

        quantityField = new JTextField(5);
        purchaseBtn = new JButton("Purchase");
        outputArea = new JTextArea(10, 30);
        outputArea.setEditable(false);

        add(new JLabel("Select Customer:"));
        add(customerBox);
        add(new JLabel("Select Product:"));
        add(productBox);
        add(new JLabel("Quantity:"));
        add(quantityField);
        add(purchaseBtn);
        add(new JScrollPane(outputArea));

        purchaseBtn.addActionListener(this);

        loadCustomers();
        loadProducts();
        
        getContentPane().setBackground(Color.lightGray);
        setSize(400, 400);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setVisible(true);
    }

    private void loadCustomers() {
        customers.clear();
        customerBox.removeAllItems();
        customerBox.addItem("Select a Customer");
        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME_CUSTOMERS))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] data = line.split(",");
                if (data.length >= 3) {
                    customers.add(data);
                    customerBox.addItem(data[1] + " " + data[2]);
                }
            }
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error loading customers.");
        }
    }

    private void loadProducts() {
        products.clear();
        productBox.removeAllItems();
        productBox.addItem("Select a Product");
        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME_PRODUCTS))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] data = line.split(",");
                if (data.length >= 3) {
                    products.add(data);
                    productBox.addItem(data[1] + " ($" + data[2] + ")");
                }
            }
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error loading products.");
        }
    }

    private void saveTransaction(String customer, String product, int quantity, double totalPrice) {

        LocalDate date = LocalDate.now();

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(ORDER_FILE, true))) {
            writer.write(customer + "," + product + "," + quantity + "," + totalPrice + "," + date);
            writer.newLine();
            outputArea.append("Transaction saved: \n" + customer + " bought " + quantity + " " + product + totalPrice + " DATE : " + date + "\n");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error saving transaction.");
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == purchaseBtn) {
            int customerIndex = customerBox.getSelectedIndex() - 1;
            int productIndex = productBox.getSelectedIndex() - 1;
            if (customerIndex < 0 || productIndex < 0) {
                JOptionPane.showMessageDialog(this, "Please select a valid customer and product.");
                return;
            }
            
            int quantity;
            try {
                quantity = Integer.parseInt(quantityField.getText());
                if (quantity <= 0) throw new NumberFormatException();
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Enter a valid quantity.");
                return;
            }
            
            String[] customer = customers.get(customerIndex);
            String[] product = products.get(productIndex);
            double price = Double.parseDouble(product[2]);
            double totalPrice = price * quantity;
            saveTransaction(customer[1] + " " + customer[2], product[1], quantity, totalPrice);
        }
    }
}


