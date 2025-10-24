# File System backup vs Snapshot backup

**Filesystem Backup (FSB)**
   A backup method that works with almost any storage type, including NFS,
   local disks, or cloud storage that does not support snapshots. Useful when
   snapshots are not available or when fine-grained control over files is
   needed.

**Snapshot Backup**
   A fast, efficient way to back up entire volumes that is tightly integrated
   with the storage provider. Ideal for cloud-native environments where CSI
   snapshots are supported.

!!! note

    * **Filesystem backups are NOT truly cross-platform** because they capture
      files and directories in a way that depends on the underlying storage
      system. If you back up on AWS, for example, restoring to Azure might not
      work smoothly.
    * **Snapshot backups are also NOT cross-platform by default** because they
      rely on storage provider technology (like AWS EBS snapshots or Azure Disk
      snapshots). However, if you use a **snapshot with a data mover**, you can
      transfer it between cloud providers, making it more portable.

## Advantages and disadvantages

| Feature | Filesystem Backup | Snapshot Backup |
|----------|------------------|-----------------|
| **Speed** | **Slower** – Reads and transfers all files, making large backups time-consuming. | **Faster** – Works at the storage level, quickly capturing an entire volume. |
| **Efficiency** | **More storage needed** – Stores files individually, which may increase backup size. | **More efficient** – Uses incremental snapshots, reducing backup size and time. |
| **Compatibility** | **Works with almost any storage** – Supports NFS, local storage, cloud object storage, etc. | **Requires CSI drivers or storage provider support** – Only works if the storage supports snapshots. |
| **Portability** | **Not fully cross-platform** – Can be tricky to restore across different storage systems. | **Cross-platform with data mover** – Can be transferred between cloud providers with extra tools. |
| **Granular restore** | **Can restore individual files** – Useful if you only need specific files. | **Restores entire volume** – No easy way to get individual files without additional tools. |


## When to use each backup type

**Use Filesystem Backup if:**

* Your storage provider **doesn't support snapshots** (e.g., NFS, EFS,
  AzureFile).
* You need to **restore specific files** instead of the whole volume.
* You want a backup that works with **different storage backends** (but not
  necessarily cross-platform).

**Use Snapshot Backup if:**

* You want a **fast and efficient** backup for large persistent volumes.
* Your storage **supports CSI snapshots** or cloud-native snapshots (e.g., AWS
  EBS, Azure Disks).
* You need **incremental backups** to reduce storage costs.
