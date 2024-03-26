namespace WinFormsApp1
{
    partial class SearchRecordForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            textBox1 = new TextBox();
            GroupCountRO = new TextBox();
            GroupLeaderRO = new TextBox();
            GroupNameRO = new TextBox();
            GroupCount = new TextBox();
            GroupLeader = new TextBox();
            GroupName = new TextBox();
            FoundButton = new Button();
            checkBox1 = new CheckBox();
            checkBox2 = new CheckBox();
            checkBox3 = new CheckBox();
            SuspendLayout();
            // 
            // textBox1
            // 
            textBox1.Location = new Point(47, 23);
            textBox1.Name = "textBox1";
            textBox1.ReadOnly = true;
            textBox1.Size = new Size(306, 31);
            textBox1.TabIndex = 0;
            textBox1.Text = "Поиск по шаблону";
            textBox1.TextAlign = HorizontalAlignment.Center;
            // 
            // GroupCountRO
            // 
            GroupCountRO.Location = new Point(65, 224);
            GroupCountRO.Name = "GroupCountRO";
            GroupCountRO.ReadOnly = true;
            GroupCountRO.Size = new Size(150, 31);
            GroupCountRO.TabIndex = 14;
            GroupCountRO.Text = "Численность";
            // 
            // GroupLeaderRO
            // 
            GroupLeaderRO.Location = new Point(65, 151);
            GroupLeaderRO.Name = "GroupLeaderRO";
            GroupLeaderRO.ReadOnly = true;
            GroupLeaderRO.Size = new Size(150, 31);
            GroupLeaderRO.TabIndex = 13;
            GroupLeaderRO.Text = "Староста";
            // 
            // GroupNameRO
            // 
            GroupNameRO.Location = new Point(65, 74);
            GroupNameRO.Name = "GroupNameRO";
            GroupNameRO.ReadOnly = true;
            GroupNameRO.Size = new Size(150, 31);
            GroupNameRO.TabIndex = 12;
            GroupNameRO.Text = "Имя группы";
            // 
            // GroupCount
            // 
            GroupCount.Location = new Point(236, 224);
            GroupCount.Name = "GroupCount";
            GroupCount.Size = new Size(150, 31);
            GroupCount.TabIndex = 17;
            // 
            // GroupLeader
            // 
            GroupLeader.Location = new Point(236, 151);
            GroupLeader.Name = "GroupLeader";
            GroupLeader.Size = new Size(150, 31);
            GroupLeader.TabIndex = 16;
            // 
            // GroupName
            // 
            GroupName.Location = new Point(236, 74);
            GroupName.Name = "GroupName";
            GroupName.Size = new Size(150, 31);
            GroupName.TabIndex = 15;
            // 
            // FoundButton
            // 
            FoundButton.Location = new Point(120, 300);
            FoundButton.Name = "FoundButton";
            FoundButton.Size = new Size(147, 61);
            FoundButton.TabIndex = 18;
            FoundButton.Text = "Найти";
            FoundButton.UseVisualStyleBackColor = true;
            FoundButton.Click += FoundButton_Click;
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(25, 80);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(22, 21);
            checkBox1.TabIndex = 19;
            checkBox1.UseVisualStyleBackColor = true;
            checkBox1.CheckedChanged += checkBox1_CheckedChanged;
            // 
            // checkBox2
            // 
            checkBox2.AutoSize = true;
            checkBox2.Location = new Point(25, 157);
            checkBox2.Name = "checkBox2";
            checkBox2.Size = new Size(22, 21);
            checkBox2.TabIndex = 20;
            checkBox2.UseVisualStyleBackColor = true;
            // 
            // checkBox3
            // 
            checkBox3.AutoSize = true;
            checkBox3.Location = new Point(25, 230);
            checkBox3.Name = "checkBox3";
            checkBox3.Size = new Size(22, 21);
            checkBox3.TabIndex = 21;
            checkBox3.UseVisualStyleBackColor = true;
            // 
            // FirstMatch
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(398, 450);
            Controls.Add(checkBox3);
            Controls.Add(checkBox2);
            Controls.Add(checkBox1);
            Controls.Add(FoundButton);
            Controls.Add(GroupCount);
            Controls.Add(GroupLeader);
            Controls.Add(GroupName);
            Controls.Add(GroupCountRO);
            Controls.Add(GroupLeaderRO);
            Controls.Add(GroupNameRO);
            Controls.Add(textBox1);
            Name = "FirstMatch";
            Text = "FirstMatch";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBox1;
        private TextBox GroupCountRO;
        private TextBox GroupLeaderRO;
        private TextBox GroupNameRO;
        private TextBox GroupCount;
        private TextBox GroupLeader;
        private TextBox GroupName;
        private Button FoundButton;
        private CheckBox checkBox1;
        private CheckBox checkBox2;
        private CheckBox checkBox3;
    }
}