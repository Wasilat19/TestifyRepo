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

public class Widgets {

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
    }

    @Test( groups = {"homePage"} )
    public void homePage() throws InterruptedException {
        driver.navigate().to(baseUrl);
        Thread.sleep(3000);

        //verify user is the homepage
        String actualHomePage = driver.getCurrentUrl();
        WebElement seleniumCT = driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/a[1]/img[1]"));

        if(seleniumCT.isDisplayed()){
            System.out.println(actualHomePage + " you are on the HomePage");
        } else {
            System.out.println(actualHomePage + " you are not on the HomePage");
        }
    }

    @Test(priority = 1)
    public void widgetsPage() throws InterruptedException {
        // Click on the Widgets tile
        WebElement widgetsTile = driver.findElement(By.xpath("//h5[contains(text(),'Widgets')]"));
        widgetsTile.click();
        Thread.sleep(3000);
    }

    @Test(priority = 2)
    public void assertWidgets(){

        // Assert that you are on the Widgets page
        WebElement widgetsHeader = driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]"));
        String expectedHeaderText = "Widgets";
        String actualHeaderText = widgetsHeader.getText();
        System.out.println(actualHeaderText + " page------");
        Assert.assertEquals(actualHeaderText, expectedHeaderText, "----This is not the Widgets page");
    }

    @AfterTest
    public void closeBrowser() {
        driver.quit();
    }

}