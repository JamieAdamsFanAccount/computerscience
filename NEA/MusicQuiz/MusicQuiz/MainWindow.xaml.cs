using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

using System.Data.SQLite;

namespace MusicQuiz
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        public static string content { get; set; }

        private void button_Click(object sender, RoutedEventArgs e)
        {
            content = "";
            if (string.IsNullOrEmpty(usernameinput.Text))
            {
                content = content + "Your username do be blank doe\n";
            }
            if (string.IsNullOrEmpty(password.Password))
            {
                content = content + "Your password do be blank doe\n";
            }
            outputbox.Content = content;
        }
    }
}
