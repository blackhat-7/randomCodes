/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package marathon;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.*;

class LinkedList {
    int hf_first = Integer.MAX_VALUE;
    int hf_second = Integer.MAX_VALUE;
    String hf_f = "Nobody";
    String hf_s = "Nobody";

    int or_first = Integer.MAX_VALUE;
    int or_second = Integer.MAX_VALUE;
    String or_f = "Nobody";
    String or_s = "Nobody";
    
    int gd_first = Integer.MAX_VALUE;
    int gd_second = Integer.MAX_VALUE;
    String gd_f = "Nobody";
    String gd_s = "Nobody";
    
    LNode head;
    LinkedList() {
        head = null;
    }

    class LNode {
        String name;
        int time;
        int type;
        LNode next;
        LNode(String n, int t, int p) {
            name = n;
            time = t;
            type = p;
            next = null;
        }
    }
    
    void add(String n, int t, int p) {
        LNode new_node = new LNode(n, t, p); 

        if (head == null) 
        { 
            head = new LNode(n, t, p); 
            find(head);
            return; 
        } 
        new_node.next = null; 

        LNode temp = head;  
        while (temp.next != null) {
            temp = temp.next; 
        }
        temp.next = new_node; 
        find(new_node);
    }
    
    void find(LNode temp) {
        if (temp.type==1) {
            if (temp.time < hf_first) {
                hf_second = hf_first;
                hf_s = hf_f;
                hf_first = temp.time;
                hf_f = temp.name;
            }
            else if (temp.time < hf_second) {
                hf_second = temp.time;
                hf_s = temp.name;
            }
        }
        else if (temp.type==2) {
            if (temp.time < or_first) {
                or_second = or_first;
                or_s = or_f;
                or_first = temp.time;
                or_f = temp.name;
            }
            else if (temp.time < or_second) {
                or_second = temp.time;
                or_s = temp.name;
            }
        }
        else {
            if (temp.time < gd_first) {
                gd_second = gd_first;
                gd_s = gd_f;
                gd_first = temp.time;
                gd_f = temp.name;
            }
            else if (temp.time < gd_second) {
                gd_second = temp.time;
                gd_s = temp.name;
            }
        }
    }
    
    String msg() {
        String s = "\nHalf Marathon (20km) : \n\n first  :  "+hf_f+" wins Rs. 2,80,000/-\n second  :  "+hf_s+" wins Rs. 2,10,000/-\n\n Open 10k Run (10km): \n\n first  :  "+or_f+" wins Rs. 1,90,000/-\n second  :  "+or_s+" wins Rs.1,50,00/-\n\n Geat Delhi Run (5km) : \n\n first  :  "+gd_f+" wins Rs. 1,35,000/-\n second  :  "+gd_s+" wins Rs.1,15,000/-";
        return s; 
   }

    void print() {
        LNode temp = head;
        while(temp != null) {
            System.out.println(temp.name + temp.time + temp.type);
            temp = temp.next;
        }
        System.out.println();
    }
}

public class Application {

    public static JPanel p_num;
    public static JLabel l_num;
    public static JTextField tf_num;
    
    public static JPanel p_name;
    public static JLabel l_name;
    public static JTextField tf_name;
    
    public static JPanel p_time;
    public static JLabel l_time;
    public static JTextField tf_time;
    

    static LinkedList ll;
    static int count = 0;
    static int num = 0;

    /**
     *
     * @param args
     */
    public static void main(String[] args) {
        
        ll = new LinkedList();
        
        JFrame frame = new JFrame("Marathon.exe");


        JPanel p_main = new JPanel();
        p_main.setLayout(new BoxLayout(p_main,BoxLayout.Y_AXIS));
        
        p_num = new JPanel();
        p_num.setLayout(new FlowLayout(FlowLayout.CENTER));
        p_main.add(p_num);

        l_num = new JLabel("Number of Runners : ");
        tf_num = new JTextField();
        tf_num.setPreferredSize(new Dimension(150,20));
        p_num.add(l_num);
        p_num.add(tf_num);

        p_name = new JPanel();
        p_name.setLayout(new FlowLayout(FlowLayout.CENTER));
        p_main.add(p_name);

        l_name = new JLabel("Name");
        tf_name = new JTextField();
        tf_name.setPreferredSize(new Dimension(150,20));
        p_name.add(l_name);
        p_name.add(tf_name);
        
        p_time = new JPanel();
        p_time.setLayout(new FlowLayout(FlowLayout.CENTER));
        p_main.add(p_time);

        l_time = new JLabel("Time");
        tf_time = new JTextField();
        tf_time.setPreferredSize(new Dimension(150,20));
        p_time.add(l_time);
        p_time.add(tf_time);


        JPanel p_type = new JPanel();
        p_type.setLayout(new FlowLayout(FlowLayout.CENTER));

        JLabel l_type = new JLabel("Marathon Type : ");

        p_type.add(l_type);

        p_main.add(p_type);

        ButtonGroup bg_type = new ButtonGroup();

        JRadioButton rb_1 = new JRadioButton("Half Marathon (20km)");
        JRadioButton rb_2 = new JRadioButton("Open 10K Run (10km)");
        JRadioButton rb_3 = new JRadioButton("Great Delhi Run (5km)");

        bg_type.add(rb_1);
        bg_type.add(rb_2);
        bg_type.add(rb_3);

        p_type.add(rb_1);
        p_type.add(rb_2);
        p_type.add(rb_3);

        rb_1.setSelected(true);
////////////////////////////////////



        JPanel p_winner = new JPanel();
        p_winner.setLayout(new FlowLayout(FlowLayout.CENTER));

        JLabel l_winner = new JLabel("WINNERS : ");
        JTextArea tf_winner = new JTextArea();
        tf_winner.setEditable(false);
        tf_winner.setPreferredSize(new Dimension(300,250));
//        tf_winner.setLineWrap(true);
        p_winner.add(l_winner);
        p_winner.add(tf_winner);
        p_main.add(p_winner);
////////////////////////////////////


        JPanel p_buttons = new JPanel();
        p_buttons.setLayout(new FlowLayout(FlowLayout.CENTER));

        JButton b_next = new JButton("Next");
        JButton b_calculate = new JButton("Calculate");
        JButton b_exit = new JButton("Exit");

        p_name.setVisible(false);
        p_time.setVisible(false);
        p_type.setVisible(false);
        p_winner.setVisible(false);
        b_calculate.setVisible(false);
        
        b_next.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                count++;
                System.out.println(count + " " + num);
                
                if (count==1) {
                    num = Integer.valueOf(tf_num.getText());
                    p_num.setVisible(false);
                    p_name.setVisible(true);
                    p_time.setVisible(true);
                    p_type.setVisible(true);
                    rb_1.setVisible(true);
                    rb_2.setVisible(true);
                    rb_3.setVisible(true);
                }
                if (count<=num+1 && count>1) {
                    String n = tf_name.getText();
                    int t = Integer.valueOf(tf_time.getText());
                    int p;
                    if (rb_1.isSelected()) {
                        p = 1;
                    }
                    else if (rb_2.isSelected()) {
                        p = 2;
                    }
                    else {
                        p = 3;
                    }
                    ll.add(n, t, p);
                    tf_name.setText("");
                    tf_time.setText("");
                    if (count==num+1) {
                        p_name.setVisible(false);
                        p_time.setVisible(false);
                        p_type.setVisible(false);
                        b_next.setVisible(false);
                        b_calculate.setVisible(true);
                    }
                }
            }
        });

        b_calculate.addActionListener((ActionEvent e) -> {
            System.out.println(e.getActionCommand());
            
            p_winner.setVisible(true);
            tf_winner.setText(ll.msg());
            b_calculate.setVisible(false);
            
        });
        
        b_exit.addActionListener((ActionEvent e) -> {
            System.out.println(e.getActionCommand());
            System.exit(0);
        });

        p_buttons.add(b_next);
        p_buttons.add(b_calculate);
        p_buttons.add(b_exit);

        p_main.add(p_buttons);
////////////////////////////////////

        frame.add(p_main);
        frame.setSize(600,600);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
////////////////////////////////////