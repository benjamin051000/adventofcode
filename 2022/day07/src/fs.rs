#![allow(dead_code)]

#[derive(Debug)]
pub enum FileType<T> {
    File(T),
    Dir(Vec<Box<File<T>>>)
}


/// In UNIX, everything is a file, including dirs, including "/"!
#[derive(Debug)]
pub struct File<T> {
    name: String,
    size: usize,
    filetype: FileType<T>
}


impl<T> File<T> {
    /// Add something to the File's children.
    pub fn add(&mut self, file: File<T>) -> Result<(), &str> {
        match &mut self.filetype {
            FileType::File(t) => Err("Can't add a file to a file. Consider turning this file into a dir."),
            FileType::Dir(children) => {
                children.push(Box::new(file));
                Ok(())
            }
        }
    }

    /// Makes a new tree, starting at "root".
    pub fn new(name: String, size: usize, filetype: FileType<T>) -> File<T> {
        File {
            name,
            size,
            filetype
        }
    }

    /// Returns the contents of this TreeNode.
    pub fn ls(&self) {
        todo!();
    }
}

#[test]
fn test_add() {
    // let mut t = TreeNode::<i32>::new("/".to_string());
    let mut root = File::new("/".to_string(), 0, FileType::Dir(Vec::<Box<File<i32>>>::new()));
    let readme = File::new("README.md".to_string(), 100, FileType::File(123));
    root.add(readme).unwrap();

    dbg!(root);
    // dbg!(&t);
    //
    // for item in t.ls() {
    //     println!("{item:?}");
    // }
    //
    assert!(false);
}
