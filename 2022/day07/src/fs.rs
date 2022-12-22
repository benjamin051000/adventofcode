#[derive(Debug)]
pub enum FileType<'a, T> {
    File {
        size: usize,
        data: T
    },
    Dir {
        contents: Vec<Box<File<'a, T>>> 
    }
}


impl<'a, T> FileType<'a, T> {
    /// Create a new Dir.
    pub fn mkdir() -> FileType<'a, T> {
        FileType::Dir{ contents: Vec::<Box<File<'a, T>>>::new() }
    }

    /// Create a new File
    pub fn touch(size: usize, data: T) -> FileType<'a, T> {
        FileType::File { size, data }

    }
}


/// In UNIX, everything is a file, including dirs, including "/"!
#[derive(Debug)]
pub struct File<'a, T> {
    pub name: String,
    pub parent: Option<&'a mut File<'a, T>>,
    pub filetype: FileType<'a, T>
}


impl<'a, T: std::fmt::Debug + std::fmt::Display> File<'a, T> {
    /// Add a File (or Dir) to the File's children.
    pub fn add(&mut self, file: File<'a, T>) -> Result<(), &str> {
        match &mut self.filetype {
            FileType::File { .. } => Err("Can't add a file to a file. Consider turning this file into a dir."),
            FileType::Dir { contents } => {
                contents.push(Box::new(file));
                Ok(())
            }
        }
    }

    /// Makes a new tree, starting at "root".
    pub fn new(name: String, filetype: FileType<'a, T>) -> File<'a, T> {
        File {
            name,
            parent: None,
            filetype
        }
    }

    /// Returns the contents of this TreeNode.
    /// Technically this is more like `ls` combined with `file`
    pub fn ls(&self) {
        match &self.filetype {
            FileType::File { size, .. } => println!("{} {}", size, self.name), 
            FileType::Dir { contents } => println!("dir {} ({} items)", self.name, contents.len())
        }
    }

    // Recursively show everything. Is this even possible in the current setup?
    pub fn tree(&self) {
        println!("{self:#?}")
    }
}


#[test]
fn test_add() {
    let readme = File::new("README".to_string(), FileType::touch(5, "hi".to_string()));
    readme.ls();

    let mut a = File::new("a".to_string(), FileType::mkdir());
    a.add(readme).unwrap();
    a.ls();

    let mut root = File::new("/".to_string(), FileType::mkdir());
    root.add(a).unwrap();
    root.ls();

    let b = File::new("virus.exe".to_string(), FileType::touch(10, "shutdown now".to_string()));
    b.ls();
    root.add(b).unwrap();

    root.ls();
    println!("------------");
    root.tree();

}

