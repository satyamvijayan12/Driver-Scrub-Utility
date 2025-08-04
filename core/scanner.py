import wmi

def get_incompatible_drivers():
    c = wmi.WMI()
    incompatible = []
    for driver in c.Win32_PnPSignedDriver():
        if "Error" in str(driver.DeviceClass) or driver.CompatID is None:
            incompatible.append((driver.DeviceName or "Unknown", driver.InfName, driver.DeviceClass))
    return incompatible
