package automation;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;
import org.openqa.selenium.chrome.ChromeDriver;

import java.time.Duration;

public class bankTest {
    public static void main(String[] args) throws InterruptedException {

        // Run automation in the Chrome WebBrowser
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\Ron\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();

        driver.get("https://parabank.parasoft.com/parabank/index.htm");  //Open Chrome browser to this webpage

        // Set up wait time
        Duration waittime = Duration.ofSeconds(5);
        WebDriverWait wait = new WebDriverWait(driver, waittime);

        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("loginPanel"))); // Wait for this element to load
        String pageTitle = driver.getTitle();

        // Assert that this is the title of the webpage
        assertEquals(pageTitle, "ParaBank | Welcome | Online Banking");

        // Assert that the text below is visible on screen
        assertEquals(driver.findElement(By.xpath("//*[@id='leftPanel']/h2")).getText(), "Customer Login");
        assertTrue(driver.findElement(By.xpath("//*[@id='leftPanel']/h2")).isDisplayed());

        // Assert that the login panel is visible
        assertTrue(driver.findElement(By.id("loginPanel")).isDisplayed());
        assertTrue(driver.findElement(By.xpath("//*[@id='loginPanel']/form")).isDisplayed());

        //Enter Log In Credentials
        driver.findElement(By.name("username")).sendKeys("john");
        driver.findElement(By.name("password")).sendKeys("demo");

        //Click the Log In button
        driver.findElement(By.cssSelector("[value='Log In']")).click();

        //Wait for the next screen to load
        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("accountTable")));

        //Make sure you are on the right page
        assertEquals(driver.getTitle(), "ParaBank | Accounts Overview");

        //Make sure the user's name is on the screen
        assertEquals(driver.findElement(By.className("smallText")).getText(), "Welcome John Smith");
        assertTrue(driver.findElement(By.className("smallText")).isDisplayed());

        //Make sure the account table is visible
        assertTrue(driver.findElement(By.id("accountTable")).isDisplayed());

        //Click the first account in the account table
        Thread.sleep(3000); // Added to prevent race condition
        String accountNumber = driver.findElement(By.xpath("//*[@id='accountTable']/tbody/tr[1]/td[1]/a")).getText();
        driver.findElement(By.xpath("//*[@id='accountTable']/tbody/tr[1]/td[1]/a")).click();

        //Wait for the next screen to load
        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("accountDetails")));

        //Make sure you are on the right page
        assertEquals(driver.getTitle(),"ParaBank | Account Activity");
        assertTrue(driver.findElement(By.className("title")).isDisplayed());
        assertEquals(driver.findElement(By.className("title")).getText(), "Account Details");
        assertTrue(driver.findElement(By.id("accountDetails")).isDisplayed());

        //Make sure the correct account number is displayed
        Thread.sleep(3000); // Added to prevent race condition
        assertEquals(driver.findElement(By.id("accountId")).getText(), accountNumber);

        //Confirm "About Us" appears on the page, then click it
        assertEquals(driver.findElement(By.xpath("//*[@id='footerPanel']/ul[1]/li[2]/a")).getText(), "About Us");
        driver.findElement(By.xpath("//*[@id='footerPanel']/ul[1]/li[2]/a")).click();

        wait.until(ExpectedConditions.titleIs("ParaBank | About Us"));

        //Make sure the proper text is displayed
        assertTrue(driver.findElement(By.className("title")).isDisplayed());
        assertEquals(driver.findElement(By.className("title")).getText(), "ParaSoft Demo Website");
        assertTrue(driver.findElement(By.xpath("//*[@id='rightPanel']/p[2]")).isDisplayed());
        assertEquals(driver.findElement(By.xpath("//*[@id='rightPanel']/p[2]")).getText(), "In other words: ParaBank is not a real bank!");

        Thread.sleep(3000);

        //Confirm "Log Out" appears on the screen, then click it
        assertTrue(driver.findElement(By.xpath("//*[@id='leftPanel']/ul/li[8]/a")).isDisplayed());
        assertEquals(driver.findElement(By.xpath("//*[@id='leftPanel']/ul/li[8]/a")).getText(), "Log Out");
        driver.findElement(By.xpath("//*[@id='leftPanel']/ul/li[8]/a")).click();

        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("loginPanel")));

        //Confirm that we are back on the Home page
        assertEquals(pageTitle, "ParaBank | Welcome | Online Banking");
        assertEquals(driver.findElement(By.xpath("//*[@id='leftPanel']/h2")).getText(), "Customer Login");
        assertTrue(driver.findElement(By.xpath("//*[@id='leftPanel']/h2")).isDisplayed());
        assertTrue(driver.findElement(By.id("loginPanel")).isDisplayed());
        assertTrue(driver.findElement(By.xpath("//*[@id='loginPanel']/form")).isDisplayed());

        Thread.sleep(3000);

        // TimeUnit.SECONDS.sleep(sleeper); // Give humans time to verify, not necessary for full automation
        driver.quit(); // End Test
    }

}
