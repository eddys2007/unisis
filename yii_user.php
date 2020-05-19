<?php
namespace app\models;

use Yii;
use yii\base\NotSupportedException;
use yii\behaviors\TimestampBehavior;
use yii\db\ActiveRecord;
use yii\web\IdentityInterface;


class User extends ActiveRecord implements IdentityInterface
{
    
    /**
     * {@inheritdoc}
     */
    public static function tableName()
    {
        return 'ztblMahasiswa';
    }

    /**
     * {@inheritdoc}
     */
    public function behaviors()
    {
        return [
            TimestampBehavior::className(),
        ];
    }

    /**
     * {@inheritdoc}
     */
    

    public function attributeLabels()
    {
        return [
            'password_hash' => 'Password',
        ];
    }

    /**
     * {@inheritdoc}
     */
    public static function findIdentity($NPK)
    {
        $user = static::findOne(['NPK' => $NPK]);
        if(count($user)) {
          return new static($user);
        }

    }

    /**
     * Finds user by username
     *
     * @param string $username
     * @return static|null
     */

    public static function findByUsername($NPK)
    {
        return static::findOne(['NPK' => $NPK]);
    }

    /**
     * {@inheritdoc}
     */
    public function getId()
    {
        return $this->getPrimaryKey();
    }

    /**
     * Validates password
     *
     * @param string $password password to validate
     * @return bool if password provided is valid for current user
     */
    public function validatePassword($password)
    {
        return $this->password === $password;
    }

    /**
     * {@inheritdoc}
     */
    public static function findIdentityByAccessToken($token, $type = null)
    {
        throw new NotSupportedException('"findIdentityByAccessToken" is not implemented.');
    }

    /**
     * {@inheritdoc}
     */
    public function getAuthKey()
    {
        return $this->NPK;
    }

    /**
     * {@inheritdoc}
     */
    public function validateAuthKey($authKey)
    {
        //return $this->getAuthKey() === $authKey;
    }

    public function getName()
    {
        return Yii::$app->user->identity->nama_lengkap;
    }
}
