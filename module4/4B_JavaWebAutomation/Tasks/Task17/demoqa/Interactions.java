package com.demoqa;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

public class Interactions {

    WebDriver driver=null;
    String baseUrl = "https://demoqa.com";

    @BeforeTest
    public  void start() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\wasilat\\wasilat-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        // Manage wait time
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        driver.get(baseUrl);
        Thread.sleep(3000);

        //System.out.println("Browser launch------");
    }

    @Test(priority = 1)
    public void interactionsPage() throws InterruptedException {
        // Click on the Interactions tile
        WebElement interactionsTile = driver.findElement(By.xpath("//h5[contains(text(),'Interactions')]"));
        interactionsTile.click();
        Thread.sleep(3000);
    }

    @Test(priority = 2)
    public void assertInteractions(){

        // Assert that you are on the Interactions page
        WebElement interactionsHeader = driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]"));
        String expectedHeaderText = "Interactions";
        String actualHeaderText = interactionsHeader.getText();
        System.out.println(actualHeaderText + " page------");
        Assert.assertEquals(actualHeaderText, expectedHeaderText, "----This is not the Interactions page");
    }

    @AfterTest
    public void closeBrowser() {
        driver.quit();
    }
}