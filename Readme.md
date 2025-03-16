# Step-by-Step Guide to Run the Project and Execute Tests
**Author: George Kplivi**

## Step 1: Set Up Your Environment

1. **Install Required Software**:
   - Ensure you have Python installed (preferably Python 3.x).
   - Install Appium and ensure the Appium server is running.
   - Install any necessary dependencies for your project, such as `pytest`, `appium-python-client`, and any other libraries specified in your `requirements.txt`.

   You can install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start Appium Server**:
   - Open a terminal and start the Appium server by running:
   ```bash
   appium
   ```

## Step 2: Configure Desired Capabilities

1. **Set Up Desired Capabilities**:
   - Ensure that your `get_desired_capabilities()` function in `resources/desired_capabilities.py` is correctly configured for your mobile device or emulator.

## Step 3: Run Tests Using Shell Scripts

1. **Navigate to Your Project Directory**:
   - Open a terminal and navigate to the root directory of your project where the `run__test.sh` scripts are located.

2. **Run All Tests**:
   - To run all tests, execute the following command:
   ```bash
   ./scripts/run__test.sh all
   ```

3. **Run Specific Tests**:
   - To run tests related to a specific task (e.g., task1), use:
   ```bash
   ./scripts/run__test.sh task1
   ```

   - Similarly, you can run other specific tasks by replacing `task1` with the desired task name.

## Step 4: Review Test Results

1. **Check Output**:
   - After running the tests, check the terminal output for results. The output will indicate whether the tests passed or failed.

2. **View Allure Reports (if applicable)**:
   - If you are using Allure for reporting, you can generate and view the reports by running:
   ```bash
   allure serve
   ```

## Additional Notes

- Ensure that your mobile device or emulator is connected and recognized by Appium.
- If you encounter any issues, check the logs in the terminal for error messages and troubleshoot accordingly.
- Make sure that the shell scripts (`run__test.sh`) have executable permissions. You can set this by running:

chmod +x run__test.sh
```
```
