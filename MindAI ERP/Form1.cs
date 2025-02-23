namespace MindAI_ERP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void karZararRaporuToolStripMenuItem_Click(object sender, EventArgs e)
        {
            LoadFormIntoPanel(new frm_kar_zarar());
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Maximized; // Uygulama açýlýrken tam ekran baþlat
            this.FormBorderStyle = FormBorderStyle.FixedDialog; // Kenarlarý sabitle
            this.MaximizeBox = false; // Büyütme butonunu kaldýr
            this.MinimizeBox = false; // Küçültme butonunu kaldýr
            LoadFormIntoPanel(new frm_main_dashboard());
        }

        // Formlarý panel1 içine yüklemek için kullanýlacak metod
        private void LoadFormIntoPanel(Form form)
        {
            panel1.Controls.Clear(); // Önceki formu temizle
            form.TopLevel = false; // Formun baðýmsýz pencere olmamasýný saðla
            form.Dock = DockStyle.Fill; // Formu panelin tamamýný kaplayacak þekilde ayarla
            panel1.Controls.Add(form); // Formu panele ekle
            form.Show(); // Formu göster
        }

        private void anasayfaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            LoadFormIntoPanel(new frm_main_dashboard());
        }

        private void analizEtToolStripMenuItem_Click(object sender, EventArgs e)
        {
            LoadFormIntoPanel(new frm_aylik_toplam_satis_kar_grafigi());
        }
    }
}