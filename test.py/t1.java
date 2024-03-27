import java.applet.Applet;
import java.awt.Graphics;
import javax.swing.*;
//package com.mycompany.mavenproject1;

/**
 *
 * @author abc
 */
public class t1 extends Applet {

    public void  paint(Graphics g) {
        super.paint(g);
       g.drawString("A simple Applet", 20, 20);
    }
}