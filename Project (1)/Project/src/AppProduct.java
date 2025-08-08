import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.ArrayList;
import javax.swing.*;

public class AppProduct extends JFrame implements ActionListener {
    private JPanel panelForm;
    private JTextField textCode, textName, textPrice, deleteIndexField;
    private JLabel label1, label2, label3, labelDelete;
    private JButton saveBtn, readBtn, deleteBtn, nextBtn, backBtn, deleteByIndexBtn;
    private JTextArea outputArea;
    private JScrollPane scrollPane;
    private Container c;
    private Font myFont = new Font("Tahoma", Font.BOLD, 15);
    private static final String FILENAME = "products.txt";

    private ArrayList<String[]> productList = new ArrayList<>();
    private int currentIndex = 0;

    public AppProduct() {
        super("Product Management");
        c = getContentPane();
        c.setLayout(new FlowLayout(FlowLayout.CENTER, 15, 15));
        guiForm();

        saveBtn = new JButton("Save Product");
        saveBtn.setFont(myFont);
        saveBtn.addActionListener(this);
        c.add(saveBtn);

        readBtn = new JButton("Read Products");
        readBtn.setFont(myFont);
        readBtn.addActionListener(this);
        c.add(readBtn);

        deleteBtn = new JButton("Delete All");
        deleteBtn.setFont(myFont);
        deleteBtn.addActionListener(this);
        c.add(deleteBtn);

        nextBtn = new JButton("Next");
        nextBtn.setFont(myFont);
        nextBtn.addActionListener(this);
        c.add(nextBtn);

        backBtn = new JButton("Back");
        backBtn.setFont(myFont);
        backBtn.addActionListener(this);
        c.add(backBtn);

        deleteByIndexBtn = new JButton("Delete Product");
        deleteByIndexBtn.setFont(myFont);
        deleteByIndexBtn.addActionListener(this);
        c.add(deleteByIndexBtn);

        labelDelete = new JLabel("Enter ID to Delete: ");
        labelDelete.setFont(myFont);
        c.add(labelDelete);

        deleteIndexField = new JTextField(5);
        deleteIndexField.setFont(myFont);
        c.add(deleteIndexField);

        outputArea = new JTextArea(10, 30);
        outputArea.setEditable(false);
        outputArea.setFont(myFont);
        scrollPane = new JScrollPane(outputArea);
        c.add(scrollPane);

        loadProducts();
        
        getContentPane().setBackground(Color.lightGray);
        setSize(500, 550);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setVisible(true);
    }

    public void guiForm() {
        panelForm = new JPanel();
        panelForm.setLayout(new GridLayout(3, 2));
        panelForm.setPreferredSize(new Dimension(400, 100));

        label1 = new JLabel("Enter Product Code: ");
        label1.setFont(myFont);
        panelForm.add(label1);
        textCode = new JTextField(10);
        textCode.setFont(myFont);
        panelForm.add(textCode);

        label2 = new JLabel("Enter Product Name: ");
        label2.setFont(myFont);
        panelForm.add(label2);
        textName = new JTextField(10);
        textName.setFont(myFont);
        panelForm.add(textName);

        label3 = new JLabel("Enter Product Price: ");
        label3.setFont(myFont);
        panelForm.add(label3);
        textPrice = new JTextField(10);
        textPrice.setFont(myFont);
        panelForm.add(textPrice);

        c.add(panelForm);
        panelForm.setBackground(null);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == saveBtn) {
            saveProduct();
        } else if (e.getSource() == readBtn) {
            displayProduct(0);
        } else if (e.getSource() == deleteBtn) {
            deleteAllProducts();
        } else if (e.getSource() == deleteByIndexBtn) {
            deleteProductByIndex();
        } else if (e.getSource() == nextBtn) {
            nextProduct();
        } else if (e.getSource() == backBtn) {
            prevProduct();
        }
    }

    public void saveProduct() {
        String codeStr = textCode.getText().trim();
        String nameStr = textName.getText().trim();
        String priceStr = textPrice.getText().trim();

        if (!codeStr.isEmpty() && !nameStr.isEmpty() && !priceStr.isEmpty()) {
            String[] product = {codeStr, nameStr, priceStr};
            productList.add(product);

            updateFile();
            JOptionPane.showMessageDialog(this, "Product saved successfully");

            textCode.setText("");
            textName.setText("");
            textPrice.setText("");
        } else {
            JOptionPane.showMessageDialog(this, "Please fill in all fields", "Warning", JOptionPane.WARNING_MESSAGE);
        }
    }

    public void loadProducts() {
        productList.clear();
        File file = new File(FILENAME);
        if (!file.exists()) return;

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] product = line.split(",");
                if (product.length == 3) {
                    productList.add(product);
                }
            }
        } catch (IOException exception) {
            JOptionPane.showMessageDialog(this, "Cannot read file", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void displayProduct(int index) {
        if (productList.isEmpty()) {
            outputArea.setText("No products available.");
            return;
        }

        if (index >= 0 && index < productList.size()) {
            currentIndex = index;
            String[] product = productList.get(index);
            outputArea.setText("Product " + (index + 1) + "/" + productList.size() + "\n");
            outputArea.append("Code: " + product[0] + "\n");
            outputArea.append("Name: " + product[1] + "\n");
            outputArea.append("Price: " + product[2] + "\n");
        }
    }

    public void deleteProductByIndex() {
        try {
            int index = Integer.parseInt(deleteIndexField.getText()) - 1;

            if (index >= 0 && index < productList.size()) {
                productList.remove(index);
                updateFile();
                JOptionPane.showMessageDialog(this, "Deleted successfully!");

                if (index >= productList.size()) {
                    index = productList.size() - 1;
                }
                displayProduct(index);
            } else {
                JOptionPane.showMessageDialog(this, "Invalid index", "Error", JOptionPane.ERROR_MESSAGE);
            }
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Please enter a valid number", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void updateFile() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILENAME, false))) {
            for (String[] product : productList) {
                writer.write(product[0] + "," + product[1] + "," + product[2]);
                writer.newLine();
            }
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error updating file", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void deleteAllProducts() {
        productList.clear();
        updateFile();
        outputArea.setText("");
        JOptionPane.showMessageDialog(this, "All records deleted", "Success", JOptionPane.INFORMATION_MESSAGE);
    }

    public void nextProduct() {
        if (currentIndex < productList.size() - 1) {
            displayProduct(currentIndex + 1);
        }
    }

    public void prevProduct() {
        if (currentIndex > 0) {
            displayProduct(currentIndex - 1);
        }
    }

}


