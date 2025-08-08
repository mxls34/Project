import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.ArrayList;
import javax.swing.*;

public class AppCustomer extends JFrame implements ActionListener {
    private JPanel panelForm;
    private JTextField textId, textName, textSurname, textPhone, deleteIndexField;
    private JLabel label1, label2, label3, label4, labelDelete;
    private JButton saveBtn, readBtn, deleteBtn, nextBtn, backBtn, deleteByIndexBtn;
    private JTextArea outputArea;
    private JScrollPane scrollPane;
    private Container c;
    private Font myFont = new Font("Tahoma", Font.BOLD, 15);
    private static final String FILENAME = "customers.txt";

    private ArrayList<String[]> customerList = new ArrayList<>();
    private int currentIndex = 0;

    public AppCustomer() {
        super("Customer Management");
        c = getContentPane();
        c.setLayout(new FlowLayout(FlowLayout.CENTER, 15, 15));
        guiForm();

        saveBtn = new JButton("Save Customer");
        saveBtn.setFont(myFont);
        saveBtn.addActionListener(this);
        c.add(saveBtn);

        readBtn = new JButton("Read Customers");
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

        deleteByIndexBtn = new JButton("Delete Customer");
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

        loadCustomers();
        setSize(500, 550);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setVisible(true);
        getContentPane().setBackground(Color.lightGray);
    }

    public void guiForm() {
        panelForm = new JPanel();
        panelForm.setLayout(new GridLayout(4, 2));
        panelForm.setPreferredSize(new Dimension(400, 150));

        label1 = new JLabel("Enter Customer ID: ");
        label1.setFont(myFont);
        panelForm.add(label1);
        textId = new JTextField(10);
        textId.setFont(myFont);
        panelForm.add(textId);

        label2 = new JLabel("Enter First Name: ");
        label2.setFont(myFont);
        panelForm.add(label2);
        textName = new JTextField(10);
        textName.setFont(myFont);
        panelForm.add(textName);

        label3 = new JLabel("Enter Surname: ");
        label3.setFont(myFont);
        panelForm.add(label3);
        textSurname = new JTextField(10);
        textSurname.setFont(myFont);
        panelForm.add(textSurname);

        label4 = new JLabel("Enter Phone Number: ");
        label4.setFont(myFont);
        panelForm.add(label4);
        textPhone = new JTextField(10);
        textPhone.setFont(myFont);
        panelForm.add(textPhone);

        c.add(panelForm);
        panelForm.setBackground(null);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == saveBtn) {
            saveCustomer();
        } else if (e.getSource() == readBtn) {
            displayCustomer(0);
        } else if (e.getSource() == deleteBtn) {
            deleteAllCustomers();
        } else if (e.getSource() == deleteByIndexBtn) {
            deleteCustomerByIndex();
        } else if (e.getSource() == nextBtn) {
            nextCustomer();
        } else if (e.getSource() == backBtn) {
            prevCustomer();
        }
    }

    public void saveCustomer() {
        String id = textId.getText().trim();
        String name = textName.getText().trim();
        String surname = textSurname.getText().trim();
        String phone = textPhone.getText().trim();

        if (!id.isEmpty() && !name.isEmpty() && !surname.isEmpty() && !phone.isEmpty()) {
            String[] customer = {id, name, surname, phone};
            customerList.add(customer);
            updateFile();
            JOptionPane.showMessageDialog(this, "Customer saved successfully");

            textId.setText("");
            textName.setText("");
            textSurname.setText("");
            textPhone.setText("");
        } else {
            JOptionPane.showMessageDialog(this, "Please fill in all fields", "Warning", JOptionPane.WARNING_MESSAGE);
        }
    }

    public void loadCustomers() {
        customerList.clear();
        File file = new File(FILENAME);
        if (!file.exists()) return;

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] customer = line.split(",");
                if (customer.length == 4) {
                    customerList.add(customer);
                }
            }
        } catch (IOException exception) {
            JOptionPane.showMessageDialog(this, "Cannot read file", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void updateFile() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILENAME, false))) {
            for (String[] customer : customerList) {
                writer.write(String.join(",", customer));
                writer.newLine();
            }
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error updating file", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void displayCustomer(int index) {
        if (customerList.isEmpty()) {
            outputArea.setText("No customers available.");
            return;
        }

        if (index >= 0 && index < customerList.size()) {
            currentIndex = index;
            String[] customer = customerList.get(index);
            outputArea.setText("Customer " + (index + 1) + "/" + customerList.size() + "\n");
            outputArea.append("ID: " + customer[0] + "\n");
            outputArea.append("Name: " + customer[1] + "\n");
            outputArea.append("Surname: " + customer[2] + "\n");
            outputArea.append("Phone: " + customer[3] + "\n");
        }
    }

    public void deleteCustomerByIndex() {
        try {
            int index = Integer.parseInt(deleteIndexField.getText()) - 1;

            if (index >= 0 && index < customerList.size()) {
                customerList.remove(index);
                updateFile();
                JOptionPane.showMessageDialog(this, "Deleted successfully!");

                if (index >= customerList.size()) {
                    index = customerList.size() - 1;
                }
                displayCustomer(index);
            } else {
                JOptionPane.showMessageDialog(this, "Invalid index", "Error", JOptionPane.ERROR_MESSAGE);
            }
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Please enter a valid number", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void deleteAllCustomers() {
        customerList.clear();
        updateFile();
        outputArea.setText("");
        JOptionPane.showMessageDialog(this, "All records deleted", "Success", JOptionPane.INFORMATION_MESSAGE);
    }

    public void nextCustomer() {
        if (currentIndex < customerList.size() - 1) {
            displayCustomer(currentIndex + 1);
        }
    }

    public void prevCustomer() {
        if (currentIndex > 0) {
            displayCustomer(currentIndex - 1);
        }
    }

}

